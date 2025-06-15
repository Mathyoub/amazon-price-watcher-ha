from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .api import AmazonPriceWatcherAPI

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Amazon Price Watcher from a config entry."""
    host = entry.data.get("host")
    hass.data[DOMAIN] = AmazonPriceWatcherAPI(hass, host=host)
    # Set up platforms (e.g., sensors)
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")