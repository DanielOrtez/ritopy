from ritopy.endpoints.account import AccountAPI
from ritopy.helpers import Platform
from ritopy.http.client import RitoHTTP
from ritopy.models.summoner import Summoner


class SummonerAPI:
    def __init__(self, client: RitoHTTP, platform: Platform):
        self.platform = platform
        self.endpoint: str = "/lol/summoner/v4/summoners/by-puuid"

        self._client = client
        self._account = AccountAPI(self._client, self.platform.region)

    async def by_puuid(self, puuid: str) -> Summoner:
        summoner = await self._client.get(self.platform, f"{self.endpoint}/{puuid}")
        return Summoner.model_validate(summoner)

    async def by_riot_id(self, game_name: str, tag_line: str) -> Summoner:
        account = await self._account.by_riot_id(game_name, tag_line)
        summoner = await self.by_puuid(account.puuid)
        return Summoner.model_validate(summoner)
