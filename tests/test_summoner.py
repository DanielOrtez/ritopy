import httpx
import pytest
import respx

from ritopy import SummonerAPI
from ritopy.helpers import Platform


@pytest.mark.anyio
async def test_summoner_success(client):
    with respx.mock:
        respx.get(
            "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Test/3095"
        ).mock(
            return_value=httpx.Response(
                200,
                json={
                    "puuid": "supersecretpuuid",
                    "gameName": "Test",
                    "tagLine": "3095",
                },
            )
        )

        respx.get(
            "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/supersecretpuuid"
        ).mock(
            return_value=httpx.Response(
                200,
                json={
                    "profileIconId": 2,
                    "revisionDate": 123812,
                    "puuid": "supersecretpuuid",
                    "summonerLevel": 842,
                },
            )
        )

        euw_summoners = SummonerAPI(client, platform=Platform.EUW)
        user = await euw_summoners.by_riot_id("Test", "3095")
        user2 = await euw_summoners.by_puuid("supersecretpuuid")

        assert user.puuid == "supersecretpuuid"
        assert user2.puuid == "supersecretpuuid"
