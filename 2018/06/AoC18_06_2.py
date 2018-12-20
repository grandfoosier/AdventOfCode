def run(input):
    coords = []
    for line in input:
        s = line.split(', ')
        coords += [[int(s[0]), int(s[1])]]
    labels = [i+1 for i in range(len(coords))]
    L = min(coords, key = lambda x : x[0])[0]
    U = min(coords, key = lambda x : x[1])[1]
    R = max(coords, key = lambda x : x[0])[0]
    D = max(coords, key = lambda x : x[1])[1]
    for c in coords:
        c[0] -= L-1; c[1] -= U-1
    W=R-L+3; H=D-U+3
    M = [[0]*W for h in range(H)]

    safe = 0
    for y in range(H):
        for x in range(W):
            dists = [abs(x-X)+abs(y-Y) for X,Y in coords]
            if sum(dists) < 10000: safe += 1
    print('safe zone size:', safe)

if __name__ == '__main__':
    with open('AoC18_06.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(input)
    print('\n')
