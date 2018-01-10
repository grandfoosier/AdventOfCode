class Mailbox(object):
    def __init__(self):
        self.q = {0:[], 1:[]}
        self.sent = {0:0, 1:0}
PO = Mailbox()

class Music(object):
    def __init__(self, name):
        fname = "AoC17_18_1.txt"
        self.Is = [line.rstrip("\n") for line in open(fname)]
        self.l = 0

        self.reg = {"p": name}
        self.name = name; self.can_go = 1

    def _snd(self, X):
        PO.q[self.name].append(self.reg[X])
        PO.sent[self.name] += 1
        Ps[1-w].can_go = 1
    def _set(self, X, Y):
        self.reg[X] = Y
    def _add(self, X, Y):
        self.reg[X] += Y
    def _mul(self, X, Y):
        self.reg[X] *= Y
    def _mod(self, X, Y):
        self.reg[X] %= Y
    def _rcv(self, X):
        if len(PO.q[1-self.name]) > 0:
            self.reg[X] = PO.q[1-self.name][0]
            PO.q[1-self.name] = PO.q[1-self.name][1:]
        else:
            self.l -= 1
            self.can_go = 0
            # print "#%i can not receive" % self.name
            # print "%i: %i" % (self.name, self.l)
            # print self.reg
            # print PO.q[1-self.name]
    def _jgz(self, X, Y):
        try:
            if int(X) > 0: self.l += Y - 1
        except:
            if self.reg[X] > 0: self.l += Y - 1
    def perform(self):
        r = self.Is[self.l]; self.l += 1
        # print "%i: %i > %s" % (self.name, self.l-1, r)

        s1 = r.find(" ")
        s2 = r[s1+1:].find(" ") + s1 + 1

        i = r[:3]
        X = r[s1+1: s1+2]
        try: X = int(X)
        except:
            if X not in self.reg: self.reg[X] = 0
        try: Y = int(r[s2+1:])
        except: Y = self.reg[r[s2+1:]]

        if   i == "snd": self._snd(X)
        elif i == "set": self._set(X, Y)
        elif i == "add": self._add(X, Y)
        elif i == "mul": self._mul(X, Y)
        elif i == "mod": self._mod(X, Y)
        elif i == "jgz": self._jgz(X, Y)
        elif i == "rcv": self._rcv(X)
        else:
            print r
            pause = raw_input("")
        # print self.reg
        # print PO.q[self.name]
        # pause = raw_input("")
A = Music(0); B = Music(1); Ps = [A, B]

w = 0
while True:
    if Ps[w].can_go == 0 and Ps[1-w].can_go == 0: break

    if Ps[w].can_go == 1: Ps[w].perform()
    else:
        w = 1-w

print ""
print "0:", A.reg
print "1:", B.reg
print "sent:", PO.sent
print "\n"
