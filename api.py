import aiohttp
from .const import DEFAULT_HOST

class AmazonPriceWatcherAPI:
    def __init__(self, hass, host=DEFAULT_HOST):
        self.hass = hass
        self.host = host

    async def get_products(self):
        url = f"{self.host}/api/products"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def get_history(self, product_id):
        url = f"{self.host}/api/history/{product_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def add_product(self, url):
        api_url = f"{self.host}/api/add"
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json={"url": url}) as resp:
                return await resp.json()

    async def remove_product(self, product_id):
        api_url = f"{self.host}/api/remove/{product_id}"
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url) as resp:
                return await resp.json()