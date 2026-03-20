from enum import Enum
from typing import Protocol


class Routing(Protocol):
    @property
    def url(self) -> str: ...


class Region(str, Enum):
    AMERICAS = "americas"
    EUROPE = "europe"
    ASIA = "asia"

    @property
    def url(self) -> str:
        return f"https://{self.value}.api.riotgames.com"


class Platform(str, Enum):
    EUW = "euw1"

    @property
    def region(self) -> Region:
        return PLATFORM_TO_REGION[self]

    @property
    def url(self) -> str:
        return f"https://{self.value}.api.riotgames.com"


PLATFORM_TO_REGION = {Platform.EUW: Region.EUROPE}
