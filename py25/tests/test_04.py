from ..solutions import solution_04

def test_read_grid():
    grid = solution_04.read_grid('test_inputs/test_input_04.txt')
    expected_grid = [
        ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'],
        ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'],
        ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'],
        ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'],
        ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'],
        ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'],
        ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'],
        ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
        ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'],
        ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.'],
    ]
    assert grid == expected_grid

def test_form_flattened_sub_grid():
    grid = solution_04.read_grid('test_inputs/test_input_04.txt')
    sub_grid = solution_04.form_flattened_sub_grid(grid, 5, 0)
    expected_sub_grid = [
        '.', '@', '@', 
        '@', '.', '@'
    ]
    assert sub_grid == expected_sub_grid

def test_can_remove():
    grid = solution_04.read_grid('test_inputs/test_input_04.txt')
    assert solution_04.can_remove(grid, 1, 1) == False # 6 neighbors
    assert solution_04.can_remove(grid, 2, 0) == True  # 3 neighbors, on side
    assert solution_04.can_remove(grid, 6, 2) == True  # 2 neighbors

def test_solve_a():
    solution_a = solution_04.solve_a('test_inputs/test_input_04.txt')
    expected_a = 13
    assert solution_a == expected_a

def test_remove_all_once():
    grid = solution_04.read_grid('test_inputs/test_input_04.txt')
    n, new_grid = solution_04.remove_all_once(grid)
    for row in new_grid:
        print(''.join(row))
    expected_n = 13
    expected_new_grid = solution_04.read_grid('test_inputs/test_input_04_after_removal.txt')
    assert n == expected_n
    assert new_grid == expected_new_grid

def test_solve_b():
    solution_s = solution_04.solve_b('test_inputs/test_input_04.txt')
    expected_s = 43
    assert solution_s == expected_s