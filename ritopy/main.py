import httpx


class RitoClient:
    def __init__(self, api_key: str, region: str):
        self.client = httpx.AsyncClient()
        self.api_key = api_key

        self.region = region
