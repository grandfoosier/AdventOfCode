import re

def run(inpt):
    size = 300
    SN = int(inpt[0])
    grid = [[((((c+10)*r+SN)*(c+10))//100)%10-5 for c in range(1, size+1)]
            for r in range(1, size+1)]

    powr = []
    best = [0, 0, -50]
    for R in range(size-2):
        powr += [[]]
        for C in range(size-2):
            powr[R] += [sum(sum(grid[r][C:C+3]) for r in range(R, R+3))]
            if powr[R][-1] > best[2]: best = [C+1, R+1, powr[R][-1]]
    print(best)

if __name__ == '__main__':
    with open('AoC18_11.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
