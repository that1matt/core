"""Config flow for Generac PWRView integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
from homeassistant.const import CONF_HOST, CONF_NAME

from .const import DOMAIN, DEFAULT_NAME
from .neurio_data import NeurioData

_LOGGER = logging.getLogger(__name__)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.

    Data has the keys from GENERAC_PWRVIEW_STEP_DATA_SCHEMA with values provided by the user.
    """
    # TODO validate the data can be used to set up a connection.
    host = data["host"]
    
    neurio_data = await NeurioData.get_local_current_sample(host)

    if not neurio_data:
        raise CannotConnect

    sensorId = neurio_data["sensorId"]
    # Return info that you want to store in the config entry.
    return {
        "sensorId": sensorId
    }


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Generac PWRView."""

    VERSION = 1

    def __init__(self):
        """Initialize a Generac PWRView flow."""
        self.host = None

    @callback
    def _async_generate_schema(self):
        """Generate schema."""
        schema = {}

        if self.host:
            print('1', vol.In([self.host]))
            schema[vol.Required(CONF_HOST, default=self.host)] = vol.In(
                [self.host]
            )
        else:
            print('2', schema)
            schema[vol.Required(CONF_HOST)] = str

        return vol.Schema(schema)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                data = user_input.copy()
                data[CONF_NAME] = DEFAULT_NAME
                return self.async_create_entry(title=data[CONF_NAME], data=data)

        return self.async_show_form(
            step_id="user",
            data_schema=self._async_generate_schema(),
            errors=errors
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""
