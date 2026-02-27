"""Config flow for the SmogTok integration."""

from __future__ import annotations

from datetime import datetime, timedelta
import logging
from typing import Any

from geopy.distance import geodesic
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_ID
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_create_clientsession
from homeassistant.helpers.selector import (
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)

from .api import SmogTokClient
from .const import ACTIVE_STATIONS_DAYS_THRESHOLD, DOMAIN, NEARBY_STATIONS_KM_RADIUS
from .exceptions import (
    SmogTokCannotConnect,
    SmogTokClientCommunicationError,
    SmogTokInvalidResponse,
    SmogTokNoDataAvailable,
)

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

        available_options = ["station_list", "station_id"]
        if self.hass.config.latitude and self.hass.config.longitude:
            available_options.insert(0, "station_geolocation")

        return self.async_show_menu(
            step_id="user",
            menu_options=available_options,
            description_placeholders={"nearby_radius": str(NEARBY_STATIONS_KM_RADIUS)},
        )

    async def get_list_of_stations(self) -> list[dict[str, Any]]:
        """Gets the list of SmogTok stations."""
        client = SmogTokClient(
            session=async_create_clientsession(self.hass),
        )
        return await client.async_get_list_of_stations()

    @staticmethod
    def get_distance_to_station(e: SelectOptionDict) -> float:
        """Returns station distance from SelectOptionDict object."""
        return float(e.get("label").split(" - ")[-1].split(" ")[0])

    def get_available_options(
        self, stations: list[dict[str, Any]], with_geolocation: bool = False
    ) -> list[SelectOptionDict]:
        """Returns stations that can be selected."""
        options: list[SelectOptionDict] = []
        timeThreshold = datetime.now() - timedelta(days=ACTIVE_STATIONS_DAYS_THRESHOLD)
        for station in stations:
            if (
                "ID" in station
                and station["ID"] > 0
                and "NAME" in station
                and station["NAME"] != ""
                and "IS_EXTERNAL" in station
                and "DT" in station
                and len(station["DT"]) == 19
                and datetime.strptime(station["DT"], "%Y-%m-%d %H:%M:%S")
                > timeThreshold
            ):
                value = str(station["ID"])
                label = f"{station['NAME']}"
                if station["IS_EXTERNAL"] != 1:
                    label += " [indoor]"
                label += f" (ID: {station['ID']})"
                if with_geolocation:
                    if "GEOLOCATION" in station and "," in station["GEOLOCATION"]:
                        distance_to_station = round(
                            geodesic(
                                station["GEOLOCATION"],
                                f"{self.hass.config.latitude},{self.hass.config.longitude}",
                            ).kilometers,
                            2,
                        )
                        if distance_to_station <= NEARBY_STATIONS_KM_RADIUS:
                            label += f" - {distance_to_station} km"
                        else:
                            continue
                    else:
                        continue
                options.append(SelectOptionDict(value=value, label=label))
        return options

    async def async_step_station_geolocation(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the station geolocation step."""
        errors: dict[str, str] = {}
        options: list[SelectOptionDict] = []
        if user_input is not None:
            selected = user_input.get("smogtok_station")
            return await self.async_step_station_id(user_input={CONF_ID: int(selected)})

        try:
            stations = await self.get_list_of_stations()
        except SmogTokClientCommunicationError:
            errors["base"] = "cannot_connect"
        except Exception:
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            options: list[SelectOptionDict] = self.get_available_options(stations, True)

            options.sort(key=SmogTokFlowHandler.get_distance_to_station)

            if options is None or len(options) == 0:
                errors["base"] = "no_nearby_stations"

        schema: vol.Schema = vol.Schema(
            {
                vol.Required("smogtok_station"): SelectSelector(
                    SelectSelectorConfig(
                        options=options,
                        mode=SelectSelectorMode.DROPDOWN,
                    ),
                )
            }
        )

        placeholders = {
            "station_number": str(len(options)),
            "nearby_radius": str(NEARBY_STATIONS_KM_RADIUS),
            "active_days": str(ACTIVE_STATIONS_DAYS_THRESHOLD),
        }

        return self.async_show_form(
            step_id="station_geolocation",
            data_schema=schema,
            errors=errors,
            description_placeholders=placeholders,
        )

    async def async_step_station_list(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the station list step."""
        errors: dict[str, str] = {}
        options: list[SelectOptionDict] = []
        if user_input is not None:
            selected = user_input.get("smogtok_station")
            return await self.async_step_station_id(user_input={CONF_ID: int(selected)})

        try:
            stations = await self.get_list_of_stations()
        except SmogTokClientCommunicationError:
            errors["base"] = "cannot_connect"
        except Exception:
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            options: list[SelectOptionDict] = self.get_available_options(
                stations, False
            )

            if options is None or len(options) == 0:
                errors["base"] = "no_stations"

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

        placeholders = {
            "active_days": str(ACTIVE_STATIONS_DAYS_THRESHOLD),
        }

        return self.async_show_form(
            step_id="station_list",
            data_schema=schema,
            errors=errors,
            description_placeholders=placeholders,
        )

    async def async_step_station_id(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the station ID step."""
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                response = await self.validate_input(user_input)
            except SmogTokCannotConnect:
                errors["base"] = "cannot_connect"
            except SmogTokInvalidResponse:
                errors["base"] = "invalid_response"
            except SmogTokNoDataAvailable:
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

        placeholders = {
            "deviceslist_url": "https://smogtok.com/deviceslist",
            "example_deviceslist_url": "https://smogtok.com/onedevice?probeId=3608",
            "example_device_id": "3608",
        }
        return self.async_show_form(
            step_id="station_id",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
            description_placeholders=placeholders,
        )

    async def validate_input(self, data: dict[str, Any]) -> dict[str, Any]:
        """Validate connection."""
        client = SmogTokClient(
            session=async_create_clientsession(self.hass),
        )
        response = await client.async_get_data(data[CONF_ID])
        if isinstance(response, dict) and response == {}:
            raise SmogTokNoDataAvailable
        if not response:
            raise SmogTokCannotConnect
        if (
            "ID" not in response
            or "NAME" not in response
            or "REGS" not in response
            or "IJP" not in response
            or "DT" not in response
        ):
            raise SmogTokInvalidResponse
        return response
