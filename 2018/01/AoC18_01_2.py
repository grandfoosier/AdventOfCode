def run():
    seen = [0]
    freq = 0
    for line in input:
        if line[0] == '+': freq += int(line[1:])
        else: freq -= int(line[1:])
        if freq not in seen: seen += [freq]
        else: return end(freq)
    toadd = 470
    while True:
        for s in seen[1:]:
            if (s + toadd) in seen: return end(s + toadd)
        toadd += 470

def end(freq):
    print('First repeat:', freq)
    return


if __name__ == '__main__':
    with open('AoC18_01_1.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run()
    print('\n')
