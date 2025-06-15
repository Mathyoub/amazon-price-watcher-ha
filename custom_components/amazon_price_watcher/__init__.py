"""Amazon Price Watcher integration for Home Assistant."""
from .const import DOMAIN
from .api import AmazonPriceWatcherAPI

async def async_setup(hass, config):
    """Set up the Amazon Price Watcher integration."""
    hass.data[DOMAIN] = AmazonPriceWatcherAPI(hass)
    return True