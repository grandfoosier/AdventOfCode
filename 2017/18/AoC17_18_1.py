class Music(object):
    def __init__(self):
        fname = "AoC17_18_1.txt"
        self.Is = [line.rstrip("\n") for line in open(fname)]
        self.l = 0
        print "\nInstructions Loaded\n"

        self.reg = {}
        self.last = 0; self.R = "no"

    def _snd(self, X):
        self.last = self.reg[X]
    def _set(self, X, Y):
        self.reg[X] = Y
    def _add(self, X, Y):
        self.reg[X] += Y
    def _mul(self, X, Y):
        self.reg[X] *= Y
    def _mod(self, X, Y):
        self.reg[X] %= Y
    def _rcv(self, X):
        if self.reg[X] != 0: self.R = self.last
    def _jgz(self, X, Y):
        if self.reg[X] > 0: self.l += Y - 1
    def perform(self):
        l = self.Is[self.l]; self.l += 1

        s1 = l.find(" ")
        s2 = l[s1+1:].find(" ") + s1 + 1

        i = l[:3]
        X = l[s1+1: s1+2]
        if X not in self.reg: self.reg[X] = 0
        try: Y = int(l[s2+1:])
        except: Y = self.reg[l[s2+1:]]

        if   i == "snd": self._snd(X)
        elif i == "set": self._set(X, Y)
        elif i == "add": self._add(X, Y)
        elif i == "mul": self._mul(X, Y)
        elif i == "mod": self._mod(X, Y)
        elif i == "jgz": self._jgz(X, Y)
        else:            self._rcv(X)
M = Music()

while M.R == "no": M.perform()
print M.R
print "\n"
