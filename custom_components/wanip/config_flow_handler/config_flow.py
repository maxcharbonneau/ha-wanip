"""
Config flow for wanip.

Simple config flow with no credentials required.
The WAN IP integration uses a public API that requires no authentication.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from custom_components.wanip.const import DOMAIN
from homeassistant import config_entries

if TYPE_CHECKING:
    from custom_components.wanip.config_flow_handler.options_flow import WANIPOptionsFlow


class WANIPConfigFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for wanip."""

    VERSION = 1

    @staticmethod
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> WANIPOptionsFlow:
        """Get the options flow for this handler."""
        from custom_components.wanip.config_flow_handler.options_flow import WANIPOptionsFlow  # noqa: PLC0415

        return WANIPOptionsFlow()

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Handle a flow initialized by the user."""
        # No credentials needed — create entry immediately
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title="WAN IP",
            data={},
        )


__all__ = ["WANIPConfigFlowHandler"]
