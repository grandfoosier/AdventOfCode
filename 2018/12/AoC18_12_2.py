def run(inpt):
    plants = '....' + inpt[0][15:] + '....'
    loffset = 4
    prev = [inpt[r][:5] for r in range(2, len(inpt))]
    nxt = [inpt[r][9] for r in range(2, len(inpt))]

    print(plants)
    for time in range( 50000000000):
        newgen = '..' + ''.join(nxt[prev.index(plants[p:p+5])]
                                for p in range(len(plants)-5)) + '....'
        plants = newgen
        if plants[1] != '.':
            plants = '..' + plants
            loffset += 2
        elif plants[2] != '.':
            plants = '.' + plants
            loffset += 1
        if plants[-1] != '.': plants = plants + '..'
        elif plants[-2] != '.': plants = plants + '.'

        plantsum = 0
        for i in range(len(plants)):
            if plants[i] == '#': plantsum += (i-loffset)
        print(plants,time+1,plantsum,end='')
        pause = input()

if __name__ == '__main__':
    with open('AoC18_12.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')

# Starting at 91 generations, the sum increases linearly by 72 per gen
# The sum at gen 100 is 9222
# The sum at gen 50,000,000,000 is 9222 + 72*(49,999,999,900)
# sum = 3600000002022
