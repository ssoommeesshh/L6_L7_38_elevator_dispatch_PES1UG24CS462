
from hypothesis import given, strategies as st
from elevator_dispatch import parse_request, total_travel, load_percent


@given(st.one_of(st.text(), st.none()))
def test_parse_request_no_crash(s):
    result = parse_request(s)
    assert result is None or isinstance(result, tuple)


@given(st.one_of(st.text(), st.none()))
def test_total_travel_no_crash(s):
    result = total_travel(s)
    assert result is None or isinstance(result, int)


@given(st.one_of(st.text(), st.none()))
def test_load_percent_no_crash(s):
    result = load_percent(s)
    assert result is None or isinstance(result, int)


@given(st.integers(-100, 100), st.integers(-100, 100))
def test_parse_request_valid(start, end):
    text = f"{start}->{end}"
    assert parse_request(text) == (start, end)


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=8))
def test_total_travel_valid(floors):
    text = ",".join(map(str, floors))
    expected = sum(
        abs(floors[i + 1] - floors[i])
        for i in range(len(floors) - 1)
    )
    assert total_travel(text) == expected


@given(
    st.integers(min_value=0, max_value=1000),
    st.integers(min_value=1, max_value=1000)
)
def test_load_percent_valid(load, capacity):
    text = f"{load} of {capacity}"
    assert load_percent(text) == load * 100 // capacity
