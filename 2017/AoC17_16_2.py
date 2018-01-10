fname = "AoC17_16_1.txt"
Steps = [line.rstrip("\n").split(",") for line in open(fname)][0]
print "\nSteps Loaded\n"

class Dance(object):
    def __init__(self, n):
        self.order = []
        for i in range(n): self.order.append(chr(i + 97))

    def _spin(self, n):
        self.order = self.order[-n:] + self.order[:-n]

    def _exchange(self, i, j):
        a, b = self.order[i], self.order[j]
        self.order[i], self.order[j] = b, a

    def _partner(self, a, b):
        i, j = self.order.index(a), self.order.index(b)
        self.order[i], self.order[j] = b, a

    def step(self, s):
        if s[0] == "s":
            self._spin(int(s[1:]))
        elif s[0] == "x":
            i = s.find("/")
            self._exchange(int(s[1:i]), int(s[i+1:]))
        else:
            i = s.find("/")
            self._partner(s[1:i], s[i+1:])

F = Dance(16)

def get_cycle_length():
    seen = [''.join(F.order)]
    while True:
        for s in Steps:
            F.step(s)
        this = ''.join(F.order)
        if this in seen: return seen
        else: seen.append(this)

print ""
seen = get_cycle_length()
l = len(seen); print "Cycle is %i dances." % l
print seen[1000000000 % l]
print "\n"
