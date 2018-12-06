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

    for y in range(H):
        for x in range(W):
            dists = [abs(x-X)+abs(y-Y) for X,Y in coords]
            m = min(dists)
            if dists.count(m) == 1:
                M[y][x] = labels[dists.index(m)]

    for x in range(W):
        if M[0][x] in labels: labels.remove(M[0][x])
        if M[H-1][x] in labels: labels.remove(M[H-1][x])
    for y in range(H):
        if M[y][0] in labels: labels.remove(M[y][0])
        if M[y][W-1] in labels: labels.remove(M[y][W-1])

    most = 0
    for label in labels:
        count = 0
        for m in M: count += m.count(label)
        print(label, '-', count)
        if count > most: most = count
    print('max:', most)

if __name__ == '__main__':
    with open('AoC18_06_1.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(input)
    print('\n')
