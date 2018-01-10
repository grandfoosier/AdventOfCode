class Elevator(object):
    def __init__(self, s):
        print "Initial state: %s" % s
        self.N = len(s)
        self.st_by_mv = {0:set([s])}
        self.all =         set([s])

    def _check_state(self, s):
        if s[0] == '0' or s[0] == '5': return False
        if s in self.all: return False

        ts = []
        for i in range(len(s)/2): ts.append((s[2*i+1], s[2*i+2]))

        gs = [g for (g, c) in ts]
        for (g, c) in ts:
            if (c != g) and (gs.count(c) > 0): return False
        return True

    def _find_mvs(self, s):
        moves = set([]); on_f = []
        for i in range(1, len(s)):
            if s[0] == s[i]: on_f.append(i)

        for i in range(len(on_f)):
            u = (str(int(s[0])+1) + s[1:on_f[i]] +
                 str(int(s[on_f[i]])+1) + s[on_f[i]+1:])
            if self._check_state(u): moves |= set([u])
            d = (str(int(s[0])-1) + s[1:on_f[i]] +
                 str(int(s[on_f[i]])-1) + s[on_f[i]+1:])
            if self._check_state(d): moves |= set([d])

            for j in range(i+1, len(on_f)):
                u = (str(int(s[0])+1) + s[1:on_f[i]] +
                     str(int(s[on_f[i]])+1) + s[on_f[i]+1:on_f[j]] +
                     str(int(s[on_f[j]])+1) + s[on_f[j]+1:])
                if self._check_state(u): moves |= set([u])
                d = (str(int(s[0])-1) + s[1:on_f[i]] +
                     str(int(s[on_f[i]])-1) + s[on_f[i]+1:on_f[j]] +
                     str(int(s[on_f[j]])-1) + s[on_f[j]+1:])
                if self._check_state(d): moves |= set([d])

        self.all |= moves
        return moves

    def _find_nxt(self):
        nxt = set([]); lvl = max(self.st_by_mv)
        for s in self.st_by_mv[lvl]: nxt |= self._find_mvs(s)
        self.st_by_mv[lvl+1] = nxt

    def solve(self):
        m = max(E.st_by_mv); print "\r%s" % m,
        last = E.st_by_mv[m]

        while ('4' * self.N) not in last:
            E._find_nxt()
            m = max(E.st_by_mv); print "\r%s" % m,
            last = E.st_by_mv[m]

        print "\rSolved in %i moves." % max(E.st_by_mv)

s0 = '12131'
    # EhHlL - elevator, hydrogen, lithium (lc is gen, UC is chip)
s1 = '11112123333'
    # EtTuUsSoOrR - thulium, plutonium, strontium, promethium, ruthenium
s2 = '111121233331111'
    # EtTuUsSoOrRlLdD - "" + elerium, dilithium
E = Elevator(s2)

print ""
E.solve()
print "\n"
