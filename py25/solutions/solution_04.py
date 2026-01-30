def read_grid(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(line.strip())
            grid.append(row)
    return grid

def form_flattened_sub_grid(grid, x, y):
    return [c for r in grid[max(0, y-1):y+2] for c in r[max(0, x-1):x+2]]

def can_remove(grid, x, y):
    sub = form_flattened_sub_grid(grid, x, y)
    n = sum([1 if c == '@' else 0 for c in sub])-1
    return n < 4

def solve_a(filename):
    grid = read_grid(filename)
    s = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '@' and can_remove(grid, x, y):
                s += 1
    return s
        
def remove_all_once(grid):
    to_remove = []
    n = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '@' and can_remove(grid, x, y):
                to_remove.append((x, y))
    for x, y in to_remove:
        grid[y][x] = 'x'
        n += 1
    return n, grid

def solve_b(filename):
    grid = read_grid(filename)
    s = 0
    while True:
        n, grid = remove_all_once(grid)
        if n == 0:
            break
        s += n
    return s

if __name__ == "__main__":
    print("A) Accessible rolls:", solve_a('inputs/input_04.txt'))
    print("B) Removed rolls:", solve_b('inputs/input_04.txt'))