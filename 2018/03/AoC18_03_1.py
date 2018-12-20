import re

def run():
    FabA = [[0] * 1000 for i in range(1000)]
    for line in input:
        sp = re.split('[@,:x]', line)
        x,y=int(sp[1]),int(sp[2])
        a,b=int(sp[3]),int(sp[4])
        for r in range(y, y + b):
            for c in range(x, x + a):
                FabA[r][c] += 1
    overlap = 0
    for r in range(1000):
        for c in range(1000):
            if FabA[r][c] > 1: overlap += 1
    print('Overlap:', overlap)

if __name__ == '__main__':
    with open('AoC18_03.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run()
    print('\n')
