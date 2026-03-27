"""Sensor platform for wanip."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.wanip.const import PARALLEL_UPDATES as PARALLEL_UPDATES
from homeassistant.components.sensor import SensorEntityDescription

from .diagnostic import ENTITY_DESCRIPTIONS as DIAGNOSTIC_DESCRIPTIONS, WANIPDiagnosticSensor
from .wan_ip import ENTITY_DESCRIPTIONS as WANIP_DESCRIPTIONS, WANIPAirQualitySensor

if TYPE_CHECKING:
    from custom_components.wanip.data import WANIPConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

# Combine all entity descriptions
ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    *WANIP_DESCRIPTIONS,
    *DIAGNOSTIC_DESCRIPTIONS,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: WANIPConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    # Add WAN IP sensor
    async_add_entities(
        WANIPAirQualitySensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in WANIP_DESCRIPTIONS
    )
    # Add diagnostic sensors
    async_add_entities(
        WANIPDiagnosticSensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in DIAGNOSTIC_DESCRIPTIONS
    )
