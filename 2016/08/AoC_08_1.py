fname = "AoC_08_1.txt"
Is = [line.rstrip('\n') for line in open(fname)]
print "\nInstructions Loaded"

class Screen(object):
    def __init__(self, W, H):
        self.n = []
        for i in range (H):
            self.n.append([0] * W)
S = Screen(50, 6)

def print_sn():
    print ""
    for i in range (len(S.n)): print S.n[i]
print_sn()

def do_rc(A, B):
    for b in range (B):
        for a in range (A):
            S.n[b][a] = 1

def do_rw(A, B):
    for i in range (B):
        S.n[A].insert(0, S.n[A][-1])
        S.n[A] = S.n[A][: -1]

def do_cl(A, B):
    temp = []
    for i in range (len(S.n)):
        temp.append(S.n[i][A])
    for i in range (len(S.n)):
        S.n[i][A] = temp[(i - B) % len(S.n)]

def read_ins(I):
    if I[: 4] == "rect":
        n_ = I.find(" "); nx = I.find("x")
        return do_rc(int(I[n_ + 1: nx]), int(I[nx + 1: ]))
    elif I.find("row") > 0:
        neq = I.find("="); nby = I.find("by")
        return do_rw(int(I[neq + 1: nby - 1]), int(I[nby + 3: ]))
    else:
        neq = I.find("="); nby = I.find("by")
        return do_cl(int(I[neq + 1: nby - 1]), int(I[nby + 3: ]))

print ""

for x in range (len(Is)):
    read_ins(Is[x])

print_sn()
print ""

total = 0
for i in range (len(S.n)):
    total += S.n[i].count(1)
print "\n ", total, "\n\n"
