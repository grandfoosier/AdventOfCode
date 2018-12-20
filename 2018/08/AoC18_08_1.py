def run(inpt):
    inpL = inpt[0].split()
    x, metasum = treeSum(inpL)
    print('sum:', metasum)

def treeSum(I):
    N_child = int(I.pop(0))
    N_meta = int(I.pop(0))
    metasum = 0
    for n in range(N_child):
        I, s = treeSum(I)
        metasum += s
    for n in range(N_meta): metasum += int(I.pop(0))
    return I, metasum

if __name__ == '__main__':
    with open('AoC18_08.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
