import httpx


class RitoHTTP:
    def __init__(self, api_key: str, region: str):
        self.api_key = api_key
        self.region = region

        self._client = httpx.AsyncClient(headers={"X-Riot-Token": self.api_key})
