"""Sensor platform for integration_blueprint."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import UnitOfPressure

from .entity import SmogTokEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import SmogTokDataUpdateCoordinator
    from .data import SmogTokConfigEntry


ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="air_quality",
        name="Air Quality",
        icon="mdi:air-filter",
        state_class=SensorStateClass.MEASUREMENT,
        translation_key="air_quality",
    ),
    SensorEntityDescription(
        key="air_quality_index",
        name="Air Quality Index",
        icon="mdi:air-filter",
        device_class=SensorDeviceClass.ENUM,
        options=["very_bad", "bad", "sufficient", "moderate", "good", "very_good"],
        translation_key="air_quality_index",
    ),
    SensorEntityDescription(
        key="temperature",
        icon="mdi:thermometer",
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        device_class=SensorDeviceClass.TEMPERATURE,
        translation_key="temperature",
    ),
    SensorEntityDescription(
        key="humidity",
        icon="mdi:water-percent",
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        device_class=SensorDeviceClass.HUMIDITY,
        translation_key="humidity",
    ),
    SensorEntityDescription(
        key="pressure",
        icon="mdi:gauge",
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfPressure.HPA,
        device_class=SensorDeviceClass.PRESSURE,
        translation_key="pressure",
    ),
    SensorEntityDescription(
        key="pm01",
        icon="mdi:molecule",
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="μg/m³",
        device_class=SensorDeviceClass.PM1,
        translation_key="pm01",
    ),
    SensorEntityDescription(
        key="pm25",
        icon="mdi:molecule",
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="μg/m³",
        device_class=SensorDeviceClass.PM25,
        translation_key="pm25",
    ),
    SensorEntityDescription(
        key="pm10",
        icon="mdi:molecule",
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="μg/m³",
        device_class=SensorDeviceClass.PM10,
        translation_key="pm10",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: SmogTokConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""

    api_data = entry.runtime_data.coordinator.data
    entities_to_add = []
    reg_names = {reg.get("REGNAME") for reg in api_data.get("REGS", [])}
    regname_mapping = {
        "temperature": "Temperatura",
        "humidity": "Wilgotność",
        "pressure": "Ciśnienie",
        "pm01": "PM 0,1",
        "pm25": "PM 2,5",
        "pm10": "PM 10",
    }
    for description in ENTITY_DESCRIPTIONS:
        key = description.key

        if (key in {"air_quality", "air_quality_index"} and "IJP" in api_data) or (
            key in regname_mapping and regname_mapping.get(key) in reg_names
        ):
            entities_to_add.append(description)

    async_add_entities(
        SmogTokSensor(
            title=entry.title,
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in entities_to_add
    )


class SmogTokSensor(SmogTokEntity, SensorEntity):
    """SmogTok Sensor class."""

    _attr_has_entity_name = True

    def __init__(
        self,
        title: str,
        coordinator: SmogTokDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator, entity_description.key)
        self.entity_description = entity_description

    @staticmethod
    def get_air_quality_index(air_quality: int) -> str | None:
        """Get AQI string from number."""
        air_quality_index = {
            0: "no_data",
            1: "very_good",
            2: "good",
            3: "moderate",
            4: "sufficient",
            5: "bad",
            6: "very_bad",
        }
        return air_quality_index.get(air_quality)

    def get_regs(self, regs: dict, regname: str, with_aqi: bool = False) -> str | None:
        """Get entity state from REGS array and updates it's attributes."""
        result = None
        for reg in regs:
            if reg.get("REGNAME") == regname:
                result = reg.get("VALUE")
                self._attr_extra_state_attributes = {"last_updated": reg.get("DT")}
                if with_aqi:
                    self._attr_extra_state_attributes.update(
                        {
                            "air_quality": reg.get("IJP"),
                            "air_quality_index": SmogTokSensor.get_air_quality_index(
                                reg.get("IJP")
                            ),
                            "percent": reg.get("PERCENT"),
                        }
                    )
                break
        return result

    @property
    def native_value(self) -> str | None:
        """Return the native value of the sensor."""
        apiData = self.coordinator.data
        if apiData is None or not isinstance(apiData, dict):
            return None

        if self.entity_description.key == "air_quality":
            air_quality = apiData.get("IJP")
            self._attr_extra_state_attributes = {"last_updated": apiData.get("DT")}
            return air_quality
        if self.entity_description.key == "air_quality_index":
            air_quality_index = SmogTokSensor.get_air_quality_index(apiData.get("IJP"))
            self._attr_extra_state_attributes = {"last_updated": apiData.get("DT")}
            return air_quality_index
        if self.entity_description.key == "temperature":
            return self.get_regs(apiData.get("REGS"), "Temperatura", False)
        if self.entity_description.key == "humidity":
            return self.get_regs(apiData.get("REGS"), "Wilgotność", False)
        if self.entity_description.key == "pressure":
            return self.get_regs(apiData.get("REGS"), "Ciśnienie", False)
        if self.entity_description.key == "pm01":
            return self.get_regs(apiData.get("REGS"), "PM 0,1", False)
        if self.entity_description.key == "pm25":
            return self.get_regs(apiData.get("REGS"), "PM 2,5", True)
        if self.entity_description.key == "pm10":
            return self.get_regs(apiData.get("REGS"), "PM 10", True)
        return None
