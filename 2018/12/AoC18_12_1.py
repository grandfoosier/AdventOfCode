def run(inpt):
    plants = '..........' + inpt[0][15:] + '.........................'
    prev = [inpt[r][:5] for r in range(2, len(inpt))]
    nxt = [inpt[r][9] for r in range(2, len(inpt))]

    print(plants)
    for time in range(20):
        newgen = '..' + ''.join(nxt[prev.index(plants[p:p+5])] for p in range(len(plants)-4)) + '..'
        plants = newgen
        print(plants)

    plantsum = 0
    for i in range(len(plants)):
        if plants[i] == '#': plantsum += (i-10)
    print(plantsum)

if __name__ == '__main__':
    with open('AoC18_12.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
