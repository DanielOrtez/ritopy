import os

import pytest

from ritopy.http.client import RitoHTTP

API_KEY = os.getenv("RIOT_API") or "API"


@pytest.fixture(autouse=True)
def client():
    return RitoHTTP(API_KEY)
