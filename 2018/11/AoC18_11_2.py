import re

def run(inpt):
    size = 300
    SN = int(inpt[0])
    best = [0, 0, 0, -50]

    for S in range(1, 300):
        grid = [[((((c+10)*r+SN)*(c+10))//100)%10-5 for c in range(1, size+1)]
                for r in range(1, size+1)]
        powr = []
        for R in range(size-S+1):
            powr += [[]]
            for C in range(size-S+1):
                powr[R] += [sum(sum(grid[r][C:C+S]) for r in range(R, R+S))]
                if powr[R][-1] > best[3]: best = [C+1, R+1, S, powr[R][-1]]
        print('\r%d'%S,best,end='')

    print(best)

if __name__ == '__main__':
    with open('AoC18_11.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
