import copy

class Constructor(object):
    def __init__(self):
        fname = "AoC17_24_1.txt"
        self.l = [line.rstrip("\n") for line in open(fname)]
        self.parts = {(0, 0): 1}
        self.bridges = []; self.scores = []

        for l in self.l:
            s = l.find('/')
            p = int(l[:s]); q = int(l[s+1:])
            a = min(p, q); b = max(p, q)
            try: self.parts[(a, b)] += 1
            except: self.parts[(a, b)] = 1

    def _find_available(self, so_far):
        yes = copy.deepcopy(self.parts)
        for t in so_far: yes[(min(t), max(t))] -= 1

        vlbl = []
        (a, b) = so_far[-1]
        for (p, q) in yes:
            if yes[(p, q)] == 0: pass
            elif p == b: vlbl.append((p, q))
            elif q == b: vlbl.append((q, p))
        return vlbl

    def _score(self, so_far):
        s = 0
        for (a, b) in so_far: s += a + b
        self.bridges.append(so_far); self.scores.append(s)

    def find_all(self, so_far):
        vlbl = self._find_available(so_far)

        if len(vlbl) == 0: self._score(so_far)
        for v in vlbl:
            self.find_all(copy.deepcopy(so_far) + [v])

C = Constructor()

print ""
so_far = [(0, 0)]
C.find_all(so_far)

i = C.scores.index(max(C.scores))
print C.bridges[i]
print ""
print C.scores[i]
print "\n"
