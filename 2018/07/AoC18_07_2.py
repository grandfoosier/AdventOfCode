def run(inpt):
    steps = {}
    for line in inpt:
        sp = line.split(' ')
        if sp[1] not in steps: steps[sp[1]] = []
        if sp[7] not in steps: steps[sp[7]] = []
        steps[sp[7]] += [sp[1]]

    time = 0
    workers = [[0,''],[0,''],[0,''],[0,''],[0,'']]
    avl = sorted(s for s in steps if steps[s] == [])
    # changed = True

    while True:
        inprog = [b for a,b in workers]
        avl = sorted(s for s in steps if
                     steps[s] == [] and s not in inprog)
        # if changed:
        #     print('time:', time, ' avl:', avl)

        for i in (i for i in range(5) if workers[i][0] == 0):
            if not avl: break
            next = avl[0]
            avl = avl[1:]
            workers[i] = [ord(next)-4, next]
        # if changed:
        #     print(workers)
        #     printDict(steps)
        #     pause = input()
        #     changed = False

        for i in range(5): workers[i][0] = max(0, workers[i][0] -1)
        time += 1

        for i in (i for i in range(5) if workers[i][0] == 0):
            if workers[i][1] != '': print(workers[i][1], end='')
            try: steps.pop(workers[i][1])
            except: continue
            for s in steps:
                if workers[i][1] in steps[s]: steps[s].remove(workers[i][1])
            workers[i][1] = ''
            # changed = True

        if len(steps) == 0: break
    print('\ntime:', time)

# def printDict(s):
#     for k in s: print(k, '-', s[k])

if __name__ == '__main__':
    with open('AoC18_07_1.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
