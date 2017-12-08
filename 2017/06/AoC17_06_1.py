fname = "AoC17_06_1.txt"
banks = [int(s) for s in [line.split() for line in open(fname)][0]]
print "\nBanks Loaded\n"

confs = [''.join(['%02x' % n for n in banks])]

def redist(b):
    n = max(b); i = b.index(n)
    j = i; m = len(b)
    b[i] = 0
    for r in range(n):
        j = (j+1) % m
        b[j] += 1
    return b

c = 0
while True:
    banks = redist(banks)
    c += 1
    bhex = ''.join(['%02x' % n for n in banks])
    if bhex in confs: break
    confs.append(bhex)

print c
print "\n"
