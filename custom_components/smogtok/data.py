"""Custom types for integration_blueprint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import SmogTokClient
    from .coordinator import SmogTokDataUpdateCoordinator

type SmogTokConfigEntry = ConfigEntry[SmogTokData]


@dataclass
class SmogTokData:
    """Data for SmogTok integration."""

    client: SmogTokClient
    coordinator: SmogTokDataUpdateCoordinator
    integration: Integration
    station_id: str
