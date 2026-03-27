"""Diagnostic sensors for wanip."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.wanip.entity import WANIPEntity
from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

if TYPE_CHECKING:
    from custom_components.wanip.coordinator import WANIPDataUpdateCoordinator

# No diagnostic sensors needed for WAN IP
ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = ()


class WANIPDiagnosticSensor(SensorEntity, WANIPEntity):
    """Diagnostic sensor class (unused)."""

    def __init__(
        self,
        coordinator: WANIPDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entity_description)

    @property
    def native_value(self) -> None:
        """Return None — no diagnostic sensors."""
        return None
