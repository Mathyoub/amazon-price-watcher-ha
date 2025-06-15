from homeassistant.helpers.entity import Entity
from homeassistant.const import CURRENCY_DOLLAR
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    api = hass.data[DOMAIN]
    products = await api.get_products()
    sensors = []
    for product in products:
        sensors.append(AmazonPriceSensor(api, product))
    async_add_entities(sensors, True)

class AmazonPriceSensor(Entity):
    def __init__(self, api, product):
        self._api = api
        self._product = product
        self._state = product.get("price")
        self._name = product.get("title") or product.get("asin")
        self._unique_id = f"amazon_price_{product.get('asin')}"
        self._attrs = {
            "asin": product.get("asin"),
            "url": product.get("url"),
            "availability": product.get("availability"),
            "last_checked": product.get("last_checked"),
        }

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return CURRENCY_DOLLAR

    @property
    def extra_state_attributes(self):
        return self._attrs

    @property
    def state_class(self):
        return "measurement"

    @property
    def device_class(self):
        return "monetary"

    async def async_update(self):
        # Refresh product info
        products = await self._api.get_products()
        for product in products:
            if product.get("asin") == self._attrs["asin"]:
                self._state = product.get("price")
                self._attrs.update({
                    "availability": product.get("availability"),
                    "last_checked": product.get("last_checked"),
                })