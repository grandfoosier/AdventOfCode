def run(inpt):
    inpL = inpt[0].split()
    x, value = treeSum(inpL)
    print('root value:', value)

def treeSum(I):
    N_child = int(I.pop(0))
    N_meta = int(I.pop(0))
    value = 0
    if N_child == 0:
        for n in range(N_meta): value += int(I.pop(0))
    else:
        cvals = []
        for n in range(N_child):
            I, v = treeSum(I)
            cvals += [v]
        for n in range(N_meta):
            i = int(I.pop(0))
            if i > 0 and i < N_child + 1: value += cvals[i-1]
    return I, value

if __name__ == '__main__':
    with open('AoC18_08_1.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
