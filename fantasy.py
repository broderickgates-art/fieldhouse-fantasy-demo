"""Small, educational PPR fantasy football demo. No production Fieldhouse models."""


def ppr_points(receptions: int, receiving_yards: float, receiving_tds: int) -> float:
    """Return full-PPR points from receiving stats, rounded to two decimals."""
    if receptions < 0 or receiving_yards < 0 or receiving_tds < 0:
        raise ValueError("Fantasy statistics must be non-negative")
    return round(receptions + receiving_yards / 10 + receiving_tds * 6, 2)


def rank_players(players: list[dict]) -> list[dict]:
    """Return a descending ranking without mutating the input."""
    return sorted(players, key=lambda player: player["projection"], reverse=True)


def recommend_starter(name_a: str, projection_a: float, name_b: str, projection_b: float) -> str:
    """Choose the higher-projected player, or report a tie."""
    if projection_a > projection_b:
        return name_a
    if projection_b > projection_a:
        return name_b
    return "TIE"


if __name__ == "__main__":
    sample_players = [
        {"name": "Player A", "projection": 21.4},
        {"name": "Player B", "projection": 18.9},
        {"name": "Player C", "projection": 23.1},
    ]
    print("PPR example:", ppr_points(7, 85, 2))
    print("Ranked:", rank_players(sample_players))
    print("Start:", recommend_starter("Player A", 21.4, "Player C", 23.1))
