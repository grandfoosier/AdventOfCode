PI = "jzgqcdpd"

class Knot_Hash(object):
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
            for j in range(16): n = n ^ self.lst[i*16 + j]
            self.dns[i] = n
    def _hexify(self):
        h = ""
        for i in range(16): h += "%02x" % self.dns[i]
        return h
    def hash(self, S):
        S += chr(17) + chr(31) + chr(73) + chr(47) + chr(23)
        for n in range(64):
            for c in S:
                self._twist(ord(c))
                self._shift(ord(c))
        self._condense()
        return self._hexify()
KH = Knot_Hash(256)

Grid = []
print ""
for i in range(128):
    l = bin(int(Knot_Hash(256).hash(
        PI + "-%i" % i), 16))[2:].zfill(128)
    Grid.append([b for b in l])
    print "\rBuilding Disk: %i%%" % (i*100/127),

# print ""
# for n in range(128): print ''.join(Grid[n])
# pause = raw_input("")

def find_region(i, j):
    if Grid[min(127,i+1)][j] == "1":
        Grid[i+1][j] = "x"
        find_region(i+1, j)
    if Grid[i][min(127,j+1)] == "1":
        Grid[i][j+1] = "x"
        find_region(i, j+1)
    if Grid[max(0,i-1)][j] == "1":
        Grid[i-1][j] = "x"
        find_region(i-1, j)
    if Grid[i][max(0,j-1)] == "1":
        Grid[i][j-1] = "x"
        find_region(i, j-1)

regions = 0
print "\n"
for i in range(128):
    for j in range(128):
        if Grid[i][j] == "1":
            Grid[i][j] = "x"; regions += 1
            find_region(i, j)

            for n in range(128):
                # print ''.join(Grid[n])
                for m in range(128):
                    if Grid[n][m] == "x": Grid[n][m] = "."
            # print ""
    print "\rDefragging: %i%%" % (i*100/127),

print "\n\nRegions:", regions
print "\n"
