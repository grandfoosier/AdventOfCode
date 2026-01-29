from ..solutions import solution_05

def test_read_input():
    fresh, available = solution_05.read_input('test_inputs/test_input_05.txt')
    expected_fresh = [[3, 5], [10, 14], [16, 20], [12, 18]]
    expected_available = [1, 5, 8, 11, 17, 32]
    assert fresh == expected_fresh
    assert available == expected_available

def test_is_fresh():
    fresh_intervals = [[3, 5], [10, 14], [16, 20], [12, 18]]
    assert solution_05.is_fresh(fresh_intervals, 4) == True
    assert solution_05.is_fresh(fresh_intervals, 9) == False
    assert solution_05.is_fresh(fresh_intervals, 12) == True
    assert solution_05.is_fresh(fresh_intervals, 15) == True
    assert solution_05.is_fresh(fresh_intervals, 21) == False

def test_solve_a():
    solution_a = solution_05.solve_a('test_inputs/test_input_05.txt')
    expected_a = 3  # 5, 11, and 17 are fresh
    assert solution_a == expected_a

def test_trim_intervals():
    intervals, _ = solution_05.read_input('test_inputs/test_input_05.txt')
    solution_05.trim_intervals(intervals)
    expected_intervals = [[3, 5], [10, 20]]
    assert intervals == expected_intervals

def test_solve_b():
    solution_b = solution_05.solve_b('test_inputs/test_input_05.txt')
    expected_b = 14  # Fresh items are 3,4,5,10,11,12,13,14,16,17,18,19,20
    assert solution_b == expected_b