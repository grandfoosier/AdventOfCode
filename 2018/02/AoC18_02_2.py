def run():
    for i in range(len(input)):
        for j in range(i):
            diff = 0
            for n in range(len(input[i])):
                if input[i][n] != input[j][n]: diff += 1
                if diff > 1: break
            if diff == 1: compare(input[i], input[j])

def compare(a, b):
    print(a +'\n'+ b)
    for n in range(len(a)):
        if a[n] == b[n]: print(a[n], end = '')
    print()

if __name__ == '__main__':
    with open('AoC18_02_1.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run()
    print('\n')
