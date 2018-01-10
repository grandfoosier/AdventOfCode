class Processor(object):
    def __init__(self):
        fname = "AoC17_23_1.txt"
        self.Is = [line.rstrip("\n") for line in open(fname)]
        self.l = 0; self.reg = {}
        self.count_M = 0

    def _set(self, X, Y):
        self.reg[X] = Y
    def _sub(self, X, Y):
        self.reg[X] -= Y
    def _mul(self, X, Y):
        self.reg[X] *= Y; self.count_M += 1
    def _jnz(self, X, Y):
        try:
            if int(X) != 0: self.l += Y - 1
        except:
            if self.reg[X] != 0: self.l += Y - 1

    def perform(self):
        try: r = self.Is[self.l]
        except: return 0
        self.l += 1

        s1 = r.find(" "); s2 = r[s1+1:].find(" ") + s1 + 1

        i = r[:3]; X = r[s1+1: s1+2]
        try: X = int(X)
        except:
            if X not in self.reg: self.reg[X] = 0
        try: Y = int(r[s2+1:])
        except: Y = self.reg[r[s2+1:]]

        if   i == "set": self._set(X, Y)
        elif i == "sub": self._sub(X, Y)
        elif i == "mul": self._mul(X, Y)
        elif i == "jnz": self._jnz(X, Y)
        else: pause = raw_input(r)

        return 1
P = Processor()

while P.perform(): pass

print ""
print "P:", P.reg, P.count_M
print "\n"
