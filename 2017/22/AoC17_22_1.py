class Virus(object):
    def __init__(self):
        fname = "AoC17_22_1.txt"
        self.grid = [line.rstrip("\n") for line in open(fname)]
        self.p = (0, 0); self.d = 'U'
        self.status = {}; self.infected = 0
        N = len(self.grid[0])
        for y in range(N):
            for x in range(N):
                self.status[(x - N/2, N/2 - y)] = self.grid[y][x]

    def _turn_l(self):
        if self.d == 'U': self.d = 'L'
        elif self.d == 'R': self.d = 'U'
        elif self.d == 'D': self.d = 'R'
        else: self.d = 'D'

    def _turn_r(self):
        if self.d == 'U': self.d = 'R'
        elif self.d == 'R': self.d = 'D'
        elif self.d == 'D': self.d = 'L'
        else: self.d = 'U'

    def _move(self):
        x, y = self.p
        if self.d == 'U': self.p = (x,y+1)
        elif self.d == 'R': self.p = (x+1,y)
        elif self.d == 'D': self.p = (x,y-1)
        else: self.p = (x-1,y)
        if self.p not in self.status: self.status[self.p] = '.'

    def _toggle(self):
        if self.status[self.p] == ".":
            self.status[self.p] = "#"; self.infected += 1
        else: self.status[self.p] = "."

    def _burst(self):
        if self.status[self.p] == ".": self._turn_l()
        else: self._turn_r()
        self._toggle()
        self._move()

    def run(self, n):
        for i in range(n): self._burst()
        return self.infected
V = Virus()

print ""
print V.run(10000)
print "\n"
