import pytest
from pyreqwest.pytest_plugin import ClientMocker

from ritopy import SummonerAPI
from ritopy.helpers import Platform


@pytest.mark.asyncio
async def test_summoner_success(client, client_mocker: ClientMocker):
    client_mocker.get(
        url="https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Test/3095"
    ).with_body_json(
        {
            "puuid": "supersecretpuuid",
            "gameName": "Test",
            "tagLine": "3095",
        }
    )

    client_mocker.get(
        url="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/supersecretpuuid"
    ).with_body_json(
        {
            "profileIconId": 2,
            "revisionDate": 123812,
            "puuid": "supersecretpuuid",
            "summonerLevel": 842,
        }
    )

    async with client as clt:
        euw_summoners = SummonerAPI(clt, platform=Platform.EUW)
        user = await euw_summoners.by_riot_id("Test", "3095")
        user2 = await euw_summoners.by_puuid("supersecretpuuid")

        assert user.puuid == "supersecretpuuid"
        assert user2.puuid == "supersecretpuuid"
