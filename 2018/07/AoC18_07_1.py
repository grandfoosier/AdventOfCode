def run(input):
    steps = {}
    for line in input:
        sp = line.split(' ')
        if sp[1] not in steps: steps[sp[1]] = []
        if sp[7] not in steps: steps[sp[7]] = []
        steps[sp[7]] += [sp[1]]

    avl = sorted(s for s in steps if steps[s] == [])
    while avl:
        next = avl[0]
        print(next, end='')
        steps.pop(next)
        for s in steps:
            if next in steps[s]: steps[s].remove(next)
        avl = sorted(s for s in steps if steps[s] == [])
    print()

if __name__ == '__main__':
    with open('AoC18_07.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(input)
    print('\n')
