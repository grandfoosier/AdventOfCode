def run(inpt):
    splt = inpt[0].split()
    P, N = int(splt[0]), int(splt[-2])
    p, n = 0, 1
    S = [0] * P
    M, m = [0], 0
    while n < N:
        if p == P: p = 0
        if n % 23 == 0:
            m = (m - 7) % len(M)
            S[p] += M[m] + n
            M.remove(M[m])
            p += 1; n += 1
        else:
            m = (m + 2) % len(M)
            if m == 0: m = len(M)
            M.insert(m, n)
            p += 1; n += 1
    print('High score is:', max(S))

if __name__ == '__main__':
    with open('AoC18_09.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
