class RpsGameError(Exception):
    pass


class WrongNumberOfPlayersError(RpsGameError):
    pass


class InvalidPlayerFormatError(RpsGameError):
    pass


class NoSuchStrategyError(RpsGameError):
    pass


STRATEGIES = {"R", "P", "S"}


def rps_game_winner(players: list[list[str]]) -> str:
    _validate_players(players)

    (player1, move1), (player2, move2) = players

    if _first_player_wins(move1, move2):
        return f"{player1} {move1}"

    return f"{player2} {move2}"


def _validate_players(players: list[list[str]]) -> None:
    if len(players) != 2:
        raise WrongNumberOfPlayersError

    for player in players:
        if len(player) != 2:
            raise InvalidPlayerFormatError

        _, move = player
        if move not in STRATEGIES:
            raise NoSuchStrategyError


def _first_player_wins(move1: str, move2: str) -> bool:
    return (
        move1 == move2
        or (move1 == "R" and move2 == "S")
        or (move1 == "S" and move2 == "P")
        or (move1 == "P" and move2 == "R")
    )
