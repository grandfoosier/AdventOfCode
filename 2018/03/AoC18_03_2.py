import re

class Fabric(object):
    def __init__(self, n):
        self.A = [[0] * n for i in range(n)]

def run():
    Fab = Fabric(1000)
    for line in input:
        sp = re.split('[@,:x]', line)
        x,y=int(sp[1]),int(sp[2])
        a,b=int(sp[3]),int(sp[4])
        for r in range(y, y + b):
            for c in range(x, x + a):
                Fab.A[r][c] += 1
    for i in range(len(input)):
        if check(input[i], Fab):
            print('Claim ID:',i+1)

def check(line, Fab):
    sp = re.split('[@,:x]', line)
    x,y=int(sp[1]),int(sp[2])
    a,b=int(sp[3]),int(sp[4])
    for r in range(y, y + b):
        for c in range(x, x + a):
            if Fab.A[r][c] > 1: return False
    return True

if __name__ == '__main__':
    with open('AoC18_03.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run()
    print('\n')
