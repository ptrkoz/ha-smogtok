"""The SmogTok integration."""

from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.loader import async_get_loaded_integration

from .api import SmogTokClient
from .const import DOMAIN
from .coordinator import SmogTokDataUpdateCoordinator
from .data import SmogTokConfigEntry, SmogTokData

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: SmogTokConfigEntry) -> bool:
    """Set up SmogTok from a config entry."""

    coordinator = SmogTokDataUpdateCoordinator(
        hass=hass, logger=_LOGGER, name=DOMAIN, update_interval=timedelta(minutes=5)
    )
    entry.runtime_data = SmogTokData(
        client=SmogTokClient(session=async_get_clientsession(hass)),
        integration=async_get_loaded_integration(hass, entry.domain),
        coordinator=coordinator,
        station_id=entry.title,
    )

    await coordinator.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: SmogTokConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(hass: HomeAssistant, entry: SmogTokConfigEntry) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
