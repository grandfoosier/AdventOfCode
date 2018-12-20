def run():
    twos, threes = 0, 0
    for line in input:
        a, b = 0, 0
        for c in set(line):
            n = line.count(c)
            if n == 2: a = 1
            elif n == 3: b = 1
        twos += a
        threes += b
    print('twos:', twos)
    print('threes:', threes)
    print(twos * threes)

if __name__ == '__main__':
    with open('AoC18_02.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run()
    print('\n')
