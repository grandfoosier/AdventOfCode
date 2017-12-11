fname = "AoC17_10_1.txt"
S = [line for line in open(fname)][0].rstrip("\n")
print "\nLengths Loaded\n"

class ListN(object):
    def __init__(self, N):
        self.lst = [i for i in range(N)]
        self.pos = 0; self.skp = 0
        self.dns = [0] * 16
    def _twist(self, L):
        t = [self.lst[(self.pos + i)%len(self.lst)] for i in range(L)]
        for i in range(L):
            self.lst[(self.pos + i)%len(self.lst)] = t[-1 - i]
    def _shift(self, L):
        self.pos = (self.pos + L + self.skp)%len(self.lst)
        self.skp += 1
    def _condense(self):
        for i in range(16):
            n = 0
            for j in range(16):
                n = n ^ self.lst[i*16 + j]
            self.dns[i] = n
    def _hexify(self):
        h = ""
        for i in range(16):
            h += "%02x" % self.dns[i]
        return h
    def hash(self, S):
        S += chr(17) + chr(31) + chr(73) + chr(47) + chr(23)
        for n in range(64):
            for c in S:
                self._twist(ord(c))
                self._shift(ord(c))
        self._condense()
        return self._hexify()
L = ListN(256)

print L.hash(S)
print "\n"
