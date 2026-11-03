
import pytest
from elevator_dispatch import next_direction, door_action, pick_elevator


# Test every direction decision
@pytest.mark.parametrize("current,direction,requests,expected", [
    (3, "up", [5, 7], "up"),
    (5, "up", [2], "down"),
    (5, "up", [], "idle"),
    (5, "down", [1, 3], "down"),
    (2, "down", [6], "up"),
    (2, "down", [], "idle"),
    (3, "idle", [8], "up"),
    (8, "idle", [3], "down"),
    (3, "idle", [], "idle"),
])
def test_next_direction(current, direction, requests, expected):
    assert next_direction(current, direction, requests) == expected


# Test every door decision and priority
@pytest.mark.parametrize("load,blocked,emergency,expected", [
    (100, True, True, "hold_open"),
    (700, True, False, "overload"),
    (100, True, False, "reopen"),
    (100, False, False, "close"),
    (630, False, False, "close"),
])
def test_door_action(load, blocked, emergency, expected):
    assert door_action(load, blocked, emergency) == expected


# Test elevator selection decisions
@pytest.mark.parametrize("cars,floor,expected", [
    ([], 5, None),
    ([("A", 2, True)], 5, "A"),
    ([("A", 2, True), ("B", 9, True)], 5, "A"),
    ([("A", 0, False), ("B", 9, True)], 7, "B"),
    ([("A", 0, True), ("B", 7, True)], 7, "B"),
    ([("A", 3, True), ("B", 7, True)], 5, "A"),
])
def test_pick_elevator(cars, floor, expected):
    assert pick_elevator(cars, floor) == expected
