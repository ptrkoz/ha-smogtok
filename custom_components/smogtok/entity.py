"""SmogTok entity class."""

from __future__ import annotations

from homeassistant.const import CONF_ID
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER, STATION_DETAILS_WEBSITE_URL
from .coordinator import SmogTokDataUpdateCoordinator


class SmogTokEntity(CoordinatorEntity[SmogTokDataUpdateCoordinator]):
    """SmogTok entity class."""

    def __init__(self, coordinator: SmogTokDataUpdateCoordinator, key: str) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{coordinator.config_entry.entry_id}_{coordinator.config_entry.data[CONF_ID]}_{key}"
        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, coordinator.config_entry.data[CONF_ID])},
            manufacturer=MANUFACTURER,
            name=coordinator.config_entry.title,
            configuration_url=STATION_DETAILS_WEBSITE_URL.format(
                station_id=coordinator.config_entry.data[CONF_ID]
            ),
        )
