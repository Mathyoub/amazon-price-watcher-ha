import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from .const import DOMAIN, DEFAULT_HOST

class AmazonPriceWatcherConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Amazon Price Watcher."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Optionally, you could test the connection here
            return self.async_create_entry(
                title="Amazon Price Watcher",
                data={CONF_HOST: user_input[CONF_HOST]},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional(CONF_HOST, default=DEFAULT_HOST): str,
            }),
            errors=errors,
        )