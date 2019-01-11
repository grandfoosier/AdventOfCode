import re

def run(inpt):
    Xs, Ys, Hs, Vs = [], [], [], []
    for line in inpt:
        splt = re.split('[<,>]', line)
        Xs += [int(splt[1])]
        Ys += [int(splt[2])]
        Hs += [int(splt[4])]
        Vs += [int(splt[5])]

    Bx, By = [x for x in Xs], [y for y in Ys]
    sprd = max(Xs) - min(Xs) + max(Ys) - min(Ys)
    while True:
        Xs = [Xs[i] + Hs[i] for i in range(len(Xs))]
        Ys = [Ys[i] + Vs[i] for i in range(len(Ys))]
        s = max(Xs) - min(Xs) + max(Ys) - min(Ys)
        if s < sprd:
            Bx, By = [x for x in Xs], [y for y in Ys]
            sprd = s
        else: break

    L, R = min(Bx), max(Bx)
    U, D = min(By), max(By)
    pos = [(Bx[i], By[i]) for i in range(len(Bx))]
    for y in range(U, D+1):
        for x in range(L, R+1):
            if (x, y) in pos: print('#', end='')
            else: print(' ', end='')
        print()

if __name__ == '__main__':
    with open('AoC18_10.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
