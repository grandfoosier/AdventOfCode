class Virus(object):
    def __init__(self):
        fname = "AoC17_22_1.txt"
        self.grid = [line.rstrip("\n") for line in open(fname)]
        self.dirs = ['U', 'R', 'D', 'L']
        self.p = (0, 0); self.d = 'U'
        self.status = {}; self.infected = 0
        N = len(self.grid[0])
        for y in range(N):
            for x in range(N):
                self.status[(x - N/2, N/2 - y)] = self.grid[y][x]

    def _move(self):
        x, y = self.p
        if self.d == 'U': self.p = (x,y+1)
        elif self.d == 'R': self.p = (x+1,y)
        elif self.d == 'D': self.p = (x,y-1)
        else: self.p = (x-1,y)
        if self.p not in self.status: self.status[self.p] = '.'

    def _cycle(self):
        if   self.status[self.p] == ".": self.status[self.p] = '-'
        elif self.status[self.p] == '-':
            self.status[self.p] = "#"; self.infected += 1
        elif self.status[self.p] == "#": self.status[self.p] = '7'
        else: self.status[self.p] = "."

    def _burst(self):
        i = self.dirs.index(self.d)
        if   self.status[self.p] == ".": self.d = self.dirs[(i-1)%4]
        elif self.status[self.p] == "#": self.d = self.dirs[(i+1)%4]
        elif self.status[self.p] == "7": self.d = self.dirs[(i+2)%4]
        self._cycle()
        self._move()

    def run(self, n):
        for i in range(n): self._burst()
        return self.infected

    def prynt(self):
        l = min([x for (x, y) in self.status])
        r = max([x for (x, y) in self.status])
        d = min([y for (x, y) in self.status])
        u = max([y for (x, y) in self.status])
        N = max(abs(l), r, abs(d), u)*2 + 1

        for y in range(N):
            print " ",
            for x in range(N):
                try: print self.status[(x - N/2, N/2 - y)],
                except: print ".",
            print "\n"
V = Virus()

print ""
# print V.run(100000)
# print ""
# V.prynt()
print V.run(10000000)
print "\n"
