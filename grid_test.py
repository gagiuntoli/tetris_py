
from copy import deepcopy

from grid import clear_rows
from colors import RED, GREEN, BLACK

def test_clear_rows_no_clear():
    original_grid = [
        [BLACK, BLACK],
        [BLACK, RED]
    ]

    result_grid = clear_rows(deepcopy(original_grid))

    assert result_grid == original_grid

def test_clear_rows_1():
    original_grid = [
        [BLACK, BLACK],
        [GREEN, RED]
    ]

    expected_grid = [
        [BLACK, BLACK],
        [BLACK, BLACK]
    ]

    result_grid = clear_rows(deepcopy(original_grid))

    assert result_grid == expected_grid

def test_clear_rows_2():
    original_grid = [
        [BLACK, RED],
        [GREEN, RED]
    ]

    expected_grid = [
        [BLACK, BLACK],
        [BLACK, RED]
    ]

    result_grid = clear_rows(deepcopy(original_grid))

    assert result_grid == expected_grid

def test_clear_rows_3():
    original_grid = [
        [BLACK, BLACK],
        [BLACK, RED],
        [GREEN, RED]
    ]

    expected_grid = [
        [BLACK, BLACK],
        [BLACK, BLACK],
        [BLACK, RED]
    ]

    result_grid = clear_rows(deepcopy(original_grid))
    print("result grid", result_grid)

    assert result_grid == expected_grid