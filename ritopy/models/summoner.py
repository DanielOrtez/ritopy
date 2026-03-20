from .base import Base


class Summoner(Base):
    puuid: str
    profile_icon_id: int
    summoner_level: int
    revision_date: int
