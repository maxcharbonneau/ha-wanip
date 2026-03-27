"""WAN IP sensor for wanip."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.wanip.entity import WANIPEntity
from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

if TYPE_CHECKING:
    from custom_components.wanip.coordinator import WANIPDataUpdateCoordinator


ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="wan_ip",
        translation_key="wan_ip",
        icon="mdi:ip-network",
        has_entity_name=True,
    ),
)


class WANIPAirQualitySensor(SensorEntity, WANIPEntity):
    """WAN IP sensor class."""

    def __init__(
        self,
        coordinator: WANIPDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entity_description)

    @property
    def native_value(self) -> str | None:
        """Return the WAN IP address."""
        if not self.coordinator.last_update_success:
            return None
        return self.coordinator.data.get("ip")

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return additional state attributes."""
        return {
            "source": "api.ipify.org",
        }

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success
