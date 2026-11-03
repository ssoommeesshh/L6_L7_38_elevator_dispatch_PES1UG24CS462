
from elevator_dispatch import next_direction, door_action, pick_elevator


# Elevator direction tests

def test_up_continues_up():
    assert next_direction(3, "up", [5, 7]) == "up"


def test_up_reverses_down():
    assert next_direction(5, "up", [2]) == "down"


def test_down_continues_down():
    assert next_direction(5, "down", [1, 3]) == "down"


def test_down_reverses_up():
    assert next_direction(2, "down", [6]) == "up"


def test_idle_starts_up():
    assert next_direction(3, "idle", [8]) == "up"


def test_idle_starts_down():
    assert next_direction(8, "idle", [3]) == "down"


# Door action tests

def test_emergency():
    assert door_action(100, False, True) == "hold_open"


def test_overload():
    assert door_action(700, False, False) == "overload"


def test_blocked_door():
    assert door_action(200, True, False) == "reopen"


def test_normal_door():
    assert door_action(200, False, False) == "close"


# Elevator selection tests

def test_pick_nearest_elevator():
    cars = [
        ("A", 2, False),
        ("B", 8, True)
    ]
    assert pick_elevator(cars, 5) == "B"
