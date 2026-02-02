def read_input(filename):
    splitters, start = [], 0
    with open(filename, 'r') as file:
        i = 0
        for line in file:
            i += 1
            if i % 2 == 0:
                continue
            chars = list(line.strip())
            if i == 1:
                start = chars.index('S')
            else:
                splitters.append(chars)
    return splitters, start

def split_by_row(splitters, row, beams):
    new_beams, splits = [], 0
    for b in beams:
        if splitters[row][b] == '^':
            new_beams.append(b-1)
            new_beams.append(b+1)
            splits += 1
        else:
            new_beams.append(b)
    return sorted(new_beams), splits

def dedup(sorted_list):
    for i in range(len(sorted_list)-1).__reversed__():
        if sorted_list[i] == sorted_list[i+1]:
            sorted_list.pop(i)

def solve_a(filename):
    splitters, start = read_input(filename)
    beams = [start]
    total_splits = 0
    for row in range(len(splitters)):
        beams, splits = split_by_row(splitters, row, beams)
        dedup(beams)
        total_splits += splits
    return total_splits

def get_bottom_row_totals(splitters):
    return [1 if c == '.' else 2 for c in splitters[-1]]

def func_up(splitters, row, timelines_below):
    new_timelines = []
    for i in range(len(splitters[row])):
        if splitters[row][i] == '^':
            total = 0
            if i-1 >= 0:
                total += timelines_below[i-1]
            if i+1 < len(splitters[row]):
                total += timelines_below[i+1]
            new_timelines.append(total)
        else:
            new_timelines.append(timelines_below[i])
    return new_timelines

def solve_b(filename):
    splitters, start = read_input(filename)
    timelines = get_bottom_row_totals(splitters)
    for row in range(len(splitters)-1).__reversed__():
        timelines = func_up(splitters, row, timelines)
    return timelines[start]

if __name__ == "__main__":
    print("A) Number of beam splits:", solve_a('inputs/input_07.txt'))
    print("B) Number of timelines:", solve_b('inputs/input_07.txt'))