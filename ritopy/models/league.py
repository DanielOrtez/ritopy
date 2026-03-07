from .base import Base


class SummonerLeague(Base):
    league_id: str
    queue_type: str
    tier: str
    rank: str
    puuid: str
    league_points: int
    wins: int
    losses: int
    veteran: bool
    inactive: bool
    fresh_blood: bool
    hot_streak: bool
