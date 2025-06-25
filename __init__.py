from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .api import AmazonPriceWatcherAPI
from .config_flow import AmazonPriceWatcherOptionsFlow

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Amazon Price Watcher from a config entry."""
    api = AmazonPriceWatcherAPI(hass)
    hass.data[DOMAIN] = api

    async def handle_add_product(call):
        url = call.data.get("url")
        await api.add_product(url)

    async def handle_remove_product(call):
        product_id = call.data.get("product_id")
        await api.remove_product(product_id)

    hass.services.async_register(DOMAIN, "add_product", handle_add_product)
    hass.services.async_register(DOMAIN, "remove_product", handle_remove_product)

    # Set up platforms (e.g., sensors)
    hass.async_create_task(
        await hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")

async def async_get_options_flow(config_entry):
    """Get the options flow for this handler."""
    return AmazonPriceWatcherOptionsFlow(config_entry)