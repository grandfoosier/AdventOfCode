def read_input(filename):
    fresh, available = [], []
    is_fresh = True
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == "":
                is_fresh = False
                continue
            if is_fresh:
                fresh.append([int(x) for x in line.strip().split('-')])
            else:
                available.append(int(line))
    return fresh, available

def is_fresh(fresh_intervals, item):
    for start, end in fresh_intervals:
        if start <= item <= end:
            return True
    return False

def solve_a(filename):
    fresh, available = read_input(filename)
    s = sum(1 for item in available if is_fresh(fresh, item))
    return s

def trim_intervals(intervals):
    i, j = 1, 0
    while i < len(intervals):
        while j < i:
            if intervals[i][0] <= intervals[j][1] + 1:
                intervals[j][1] = max(intervals[j][1], intervals[i][1])
                intervals.pop(i)
                i = j
                break
            j += 1
        i += 1
        j = 0

def solve_b(filename):
    fresh, available = read_input(filename)
    fresh.sort()
    trim_intervals(fresh)
    s = sum(y-x+1 for x, y in fresh)
    return s

if __name__ == "__main__":
    print("A) Number of fresh ingredients:", solve_a('inputs/input_05.txt'))
    print("B) Total possible fresh ingredients:", solve_b('inputs/input_05.txt'))