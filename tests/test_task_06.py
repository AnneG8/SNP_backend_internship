import pytest

from task_06 import (
    InvalidPlayerFormatError,
    NoSuchStrategyError,
    WrongNumberOfPlayersError,
    rps_game_winner,
)


@pytest.mark.parametrize(
    "players, expected",
    [
        ([["player1", "P"], ["player2", "S"]], "player2 S"),
        ([["player1", "R"], ["player2", "S"]], "player1 R"),
        ([["player1", "S"], ["player2", "P"]], "player1 S"),
        ([["player1", "P"], ["player2", "P"]], "player1 P"),
    ],
)
def test_rps_game_winner_success(players, expected):
    assert rps_game_winner(players) == expected


@pytest.mark.parametrize(
    "players",
    [
        [],
        [["player1", "R"]],
        [["player1", "R"], ["player2", "S"], ["player3", "P"]],
    ],
)
def test_wrong_number_of_players(players):
    with pytest.raises(WrongNumberOfPlayersError):
        rps_game_winner(players)


@pytest.mark.parametrize(
    "players",
    [
        [["player1", "R"], ["player2"]],
        [["player1", "R", "extra"], ["player2", "S"]],
    ],
)
def test_invalid_player_format(players):
    with pytest.raises(InvalidPlayerFormatError):
        rps_game_winner(players)


@pytest.mark.parametrize(
    "players",
    [
        [["player1", "A"], ["player2", "S"]],
        [["player1", ""], ["player2", "P"]],
    ],
)
def test_no_such_strategy(players):
    with pytest.raises(NoSuchStrategyError):
        rps_game_winner(players)
