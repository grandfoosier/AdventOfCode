from ..solutions import solution_07

def test_read_input():
    splitters, start = solution_07.read_input('test_inputs/test_input_07.txt')
    expected_splitters = [
        ['.', '.', '.', '.', '.', '.', '.', '^', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '^', '.', '^', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '^', '.', '^', '.', '^', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '^', '.', '^', '.', '.', '.', '^', '.', '.', '.', '.'],
        ['.', '.', '.', '^', '.', '^', '.', '.', '.', '^', '.', '^', '.', '.', '.'],
        ['.', '.', '^', '.', '.', '.', '^', '.', '.', '.', '.', '.', '^', '.', '.'],
        ['.', '^', '.', '^', '.', '^', '.', '^', '.', '^', '.', '.', '.', '^', '.']
    ]
    expected_start = 7
    assert splitters == expected_splitters
    assert start == expected_start

def test_split_by_row():
    splitters, start = solution_07.read_input('test_inputs/test_input_07.txt')
    beams = [start]
    beams, splits = solution_07.split_by_row(splitters, 0, beams)
    expected_beams_after_row_0 = [6, 8]
    assert beams == expected_beams_after_row_0
    assert splits == 1
    beams = [3, 5, 7, 8, 9, 11]
    beams, splits = solution_07.split_by_row(splitters, 4, beams)
    expected_beams_after_row_4 = [2, 4, 4, 6, 7, 8, 8, 10, 10, 12]
    assert beams == expected_beams_after_row_4
    assert splits == 4

def test_dedup():
    sorted_list = [1, 2, 2, 3, 4, 4, 4, 5]
    expected_deduped = [1, 2, 3, 4, 5]
    solution_07.dedup(sorted_list)
    assert sorted_list == expected_deduped

def test_solve_a():
    solution_a = solution_07.solve_a('test_inputs/test_input_07.txt')
    expected_a = 21
    assert solution_a == expected_a

def test_get_bottom_row_totals():
    splitters, start = solution_07.read_input('test_inputs/test_input_07.txt')
    bottom_row_totals = solution_07.get_bottom_row_totals(splitters)
    expected_totals = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1]
    assert bottom_row_totals == expected_totals

def test_func_up():
    splitters, start = solution_07.read_input('test_inputs/test_input_07.txt')
    timelines_below = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1]
    new_timelines = solution_07.func_up(splitters, 5, timelines_below)
    expected_new_timelines = [1, 2, 4, 2, 1, 2, 4, 2, 1, 2, 1, 1, 3, 2, 1]
    assert new_timelines == expected_new_timelines

def test_solve_b():
    solution_b = solution_07.solve_b('test_inputs/test_input_07.txt')
    expected_b = 40
    assert solution_b == expected_b