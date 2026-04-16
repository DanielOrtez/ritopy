import os

import pytest_asyncio

from ritopy.http.client import RitoHTTP

API_KEY = os.getenv("RIOT_API") or "API"


@pytest_asyncio.fixture(autouse=True)
async def client():
    yield RitoHTTP(API_KEY)
