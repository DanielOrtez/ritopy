from ritopy.helpers import Region
from ritopy.http.client import RitoHTTP
from ritopy.models.account import Account


class AccountAPI:
    def __init__(self, client: RitoHTTP, region: Region):
        self.region = region
        self.endpoint = "/riot/account/v1/accounts/by-riot-id"

        self._client = client

    async def by_riot_id(self, game_name: str, tag_line: str) -> Account:
        data = await self._client.get(
            self.region, f"{self.endpoint}/{game_name}/{tag_line}"
        )
        return Account(**data)
