import httpx

from ritopy.helpers import Routing


class RitoHTTP:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._client = httpx.AsyncClient(headers={"X-Riot-Token": self._api_key})

    async def get(self, platform: Routing, path: str) -> dict:
        request = await self._client.get(f"{platform.url}{path}")
        return request.json()

    async def close(self) -> None:
        await self._client.aclose()
        return None

    async def __aexit__(self):
        await self.close()
