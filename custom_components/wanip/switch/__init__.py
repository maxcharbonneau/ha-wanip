"""Switch platform for wanip."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.wanip.const import PARALLEL_UPDATES as PARALLEL_UPDATES
from homeassistant.components.switch import SwitchEntityDescription

from .example_switch import ENTITY_DESCRIPTIONS as SWITCH_DESCRIPTIONS, WANIPSwitch

if TYPE_CHECKING:
    from custom_components.wanip.data import WANIPConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

# Combine all entity descriptions from different modules
ENTITY_DESCRIPTIONS: tuple[SwitchEntityDescription, ...] = (*SWITCH_DESCRIPTIONS,)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: WANIPConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the switch platform."""
    async_add_entities(
        WANIPSwitch(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in SWITCH_DESCRIPTIONS
    )
