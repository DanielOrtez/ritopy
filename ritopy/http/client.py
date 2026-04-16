from pyreqwest.client import ClientBuilder

from ritopy.helpers import Routing


class RitoHTTP:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._client = (
            ClientBuilder()
            .default_headers({"X-Riot-Token": self._api_key})
            .error_for_status(True)
            .build()
        )

    async def get(self, platform: Routing, path: str) -> dict:
        response = await self._client.get(f"{platform.url}{path}").build().send()
        return await response.json()

    async def close(self) -> bool:
        await self._client.close()
        return False

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return await self.close()
