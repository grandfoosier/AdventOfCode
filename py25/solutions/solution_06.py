from functools import reduce

def remove_spaces_from_line(line):
    return [x for x in line.strip().split(' ') if x != '']

def read_input(filename):
    problems = []
    with open(filename, 'r') as file:
        for line in file:
            if problems == []:
                problems = [[int(x)] for x in remove_spaces_from_line(line)]
            else:
                next = remove_spaces_from_line(line)
                if next[0] in ['+', '*']:
                    for i in range(len(problems)):
                        problems[i].insert(0, next[i])
                else:
                    for i in range(len(problems)):
                        problems[i].append(int(next[i]))
    return problems 

def solve_a(filename):
    problems = read_input(filename)
    s = 0
    for problem in problems:
        if problem[0] == '+':
            s += reduce(lambda x, y: x + y, problem[1:])
        elif problem[0] == '*':
            s += reduce(lambda x, y: x * y, problem[1:])
    return s

def read_input_sideways(filename):
    problems = []
    with open(filename, 'r') as file:
        lines = []
        for line in file:
            lines.append(line.rstrip('\n'))
        i = 0
        problem = []  # operator
        while i < len(lines[0]):
            if lines[-1][i] in ['+', '*']:
                if problem != []:
                    problems.append(problem)
                problem = [lines[-1][i]]  # operator
            to_add = ''.join([lines[j][i] for j in range(len(lines)-1) if lines[j][i] != ' '])
            if to_add != '':
                problem.append(int(to_add))
            i += 1
        problems.append(problem)
    return problems

def solve_b(filename):
    problems = read_input_sideways(filename)
    s = 0
    for problem in problems:
        if problem[0] == '+':
            s += reduce(lambda x, y: x + y, problem[1:])
        elif problem[0] == '*':
            s += reduce(lambda x, y: x * y, problem[1:])
    return s

if __name__ == "__main__":
    print("A) Grand total:", solve_a('inputs/input_06.txt'))
    print("B) Grand total:", solve_b('inputs/input_06.txt'))