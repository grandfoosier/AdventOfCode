def run():
    freq = 0
    for line in input:
        if line[0] == '+': freq += int(line[1:])
        else: freq -= int(line[1:])
    print('frequency:', freq)

if __name__ == '__main__':
    with open('AoC18_01_1.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run()
    print('\n')
