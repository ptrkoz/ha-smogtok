"""Config flow for the SmogTok integration."""

from __future__ import annotations

from datetime import datetime, timedelta
import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_ID
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_create_clientsession
from homeassistant.helpers.selector import (
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)

from .api import SmogTokClient
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ID): cv.positive_int,
    }
)


class SmogTokFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SmogTok."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        return self.async_show_menu(
            step_id="user",
            menu_options=[
                "station_list",
                "station_id",
            ],
        )

    async def async_step_station_list(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the station list step."""
        errors: dict[str, str] = {}
        if user_input is not None:
            selected = user_input.get("smogtok_station")
            return await self.async_step_station_id(user_input={CONF_ID: int(selected)})

        client = SmogTokClient(
            session=async_create_clientsession(self.hass),
        )
        stations = await client.async_get_list_of_stations()

        timeThreshold = datetime.now() - timedelta(days=30)
        options: list[SelectOptionDict] = [
            SelectOptionDict(
                value=str(station["ID"]),
                label=f"{station['NAME']} (ID: {station['ID']})",
            )
            for station in stations
            if "ID" in station
            and station["ID"] > 0
            and "NAME" in station
            and station["NAME"] != ""
            and "DT" in station
            and len(station["DT"]) == 19
            and datetime.strptime(station["DT"], "%Y-%m-%d %H:%M:%S") > timeThreshold
        ]

        schema: vol.Schema = vol.Schema(
            {
                vol.Required("smogtok_station"): SelectSelector(
                    SelectSelectorConfig(
                        options=options,
                        sort=True,
                        mode=SelectSelectorMode.DROPDOWN,
                    ),
                )
            }
        )

        return self.async_show_form(
            step_id="station_list", data_schema=schema, errors=errors
        )

    async def async_step_station_id(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the station ID step."""
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                response = await self.validate_input(user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidResponse:
                errors["base"] = "invalid_response"
            except NoDataAvailable:
                errors["base"] = "no_data_available"
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                await self.async_set_unique_id(
                    str(user_input[CONF_ID]), raise_on_progress=False
                )
                self._abort_if_unique_id_configured()

                return self.async_create_entry(title=response["NAME"], data=user_input)

        return self.async_show_form(
            step_id="station_id", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )

    async def validate_input(self, data: dict[str, Any]) -> dict[str, Any]:
        """Validate connection."""
        client = SmogTokClient(
            session=async_create_clientsession(self.hass),
        )
        response = await client.async_get_data(data[CONF_ID])
        if isinstance(response, dict) and response == {}:
            raise NoDataAvailable
        if not response:
            raise CannotConnect
        if (
            "ID" not in response
            or "NAME" not in response
            or "REGS" not in response
            or "IJP" not in response
            or "DT" not in response
        ):
            raise InvalidResponse
        return response


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class NoDataAvailable(HomeAssistantError):
    """Error to indicate there's no data available for that station."""


class InvalidResponse(HomeAssistantError):
    """Error to indicate there is invalid response."""
