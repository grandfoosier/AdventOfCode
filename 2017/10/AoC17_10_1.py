fname = "AoC17_10_1.txt"
Ls = [int(s) for s in [line.split(",") for line in open(fname)][0]]
print "\nLengths Loaded\n"

class ListN(object):
    def __init__(self, N):
        self.lst = [i for i in range(N)]
        self.pos = 0
        self.skp = 0
    def twist(self, L):
        t = [self.lst[(self.pos + i)%len(self.lst)] for i in range(L)]
        for i in range(L):
            self.lst[(self.pos + i)%len(self.lst)] = t[-1 - i]
    def shift(self, L):
        self.pos = (self.pos + L + self.skp)%len(self.lst)
        self.skp += 1
L = ListN(256)

for x in Ls:
    L.twist(x)
    L.shift(x)

print L.lst[0] * L.lst[1]
print "\n"
