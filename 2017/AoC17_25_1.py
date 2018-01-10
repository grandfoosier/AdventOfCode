class Turing(object):
    def __init__(self, N):
        self.state = 'A'; self.N = N
        self.tape = {0: 0}; self.cursor = 0

    def _A(self):
        if self.tape[self.cursor]:
            self.tape[self.cursor] = 0; self.cursor -= 1; self.state = 'C'
        else:
            self.tape[self.cursor] = 1; self.cursor += 1; self.state = 'B'
    def _B(self):
        if self.tape[self.cursor]:
            self.tape[self.cursor] = 1; self.cursor += 1; self.state = 'D'
        else:
            self.tape[self.cursor] = 1; self.cursor -= 1; self.state = 'A'
    def _C(self):
        if self.tape[self.cursor]:
            self.tape[self.cursor] = 0; self.cursor -= 1; self.state = 'E'
        else:
            self.tape[self.cursor] = 1; self.cursor += 1; self.state = 'A'
    def _D(self):
        if self.tape[self.cursor]:
            self.tape[self.cursor] = 0; self.cursor += 1; self.state = 'B'
        else:
            self.tape[self.cursor] = 1; self.cursor += 1; self.state = 'A'
    def _E(self):
        if self.tape[self.cursor]:
            self.tape[self.cursor] = 1; self.cursor -= 1; self.state = 'C'
        else:
            self.tape[self.cursor] = 1; self.cursor -= 1; self.state = 'F'
    def _F(self):
        if self.tape[self.cursor]:
            self.tape[self.cursor] = 1; self.cursor += 1; self.state = 'A'
        else:
            self.tape[self.cursor] = 1; self.cursor += 1; self.state = 'D'

    def _step(self):
        if   self.state == 'A': self._A()
        elif self.state == 'B': self._B()
        elif self.state == 'C': self._C()
        elif self.state == 'D': self._D()
        elif self.state == 'E': self._E()
        elif self.state == 'F': self._F()
        else: pause = raw_input("What did you do?")

        # print ""
        # L = min(T.tape); U = max(T.tape)
        # print " ",
        # for i in range(L, U+1): print "\b%i" % T.tape[i],

        try: t = self.tape[self.cursor]
        except: self.tape[self.cursor] = 0

    def diagnostic(self):
        for i in range(self.N): self._step()
        return sum([self.tape[k] for k in self.tape])
T = Turing(12173597)

print ""
print T.diagnostic()
print "\n"
