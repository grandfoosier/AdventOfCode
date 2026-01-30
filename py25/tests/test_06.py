from ..solutions import solution_06

def test_remove_spaces_from_line():
    line = "  123  456   789 "
    result = solution_06.remove_spaces_from_line(line)
    expected = ['123', '456', '789']
    assert result == expected

def test_read_input():
    problems = solution_06.read_input('test_inputs/test_input_06.txt')
    expected_problems = [['*', 123, 45, 6], 
                         ['+', 328, 64, 98], 
                         ['*', 51, 387, 215], 
                         ['+', 64, 23, 314]]
    assert problems == expected_problems

def test_solve_a():
    solution_a = solution_06.solve_a('test_inputs/test_input_06.txt')
    assert solution_a == 4277556

def test_read_input_sideways():
    problems = solution_06.read_input_sideways('test_inputs/test_input_06.txt')
    expected_problems = [['*', 1, 24, 356],
                         ['+', 369, 248, 8],
                         ['*', 32, 581, 175],
                         ['+', 623, 431, 4]]
    assert problems == expected_problems

def test_solve_b():
    solution_b = solution_06.solve_b('test_inputs/test_input_06.txt')
    assert solution_b == 3263827