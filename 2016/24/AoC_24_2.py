#######################################################################
# Setup
class Maze(object):
    def __init__(self):
        self.z = []
        self.Ns = []
        for i in range (37): self.Ns.append([])
        for i in range (37):
            for j in range (179): self.Ns[i].append(-1)
        self.P = [(0, 0)] * 8
        self.Rs = []
        self.Ds = []
M = Maze()

def load():
    fname = "AoC_24_1.txt"
    M.z = [line.rstrip('\n') for line in open(fname)]
    for y in range (len(M.z)):
        for x in range (len(M.z[0])):
            try:
                M.P[int(M.z[y][x])] = (x, y)
                M.z[y] = M.z[y][: x] + "." + M.z[y][x+1: ]
            except: pass

def clear():
    for i in range (37):
        for j in range (179): M.Ns[i][j] = -1

#######################################################################
#
def find_route():
    for n in range (333):
        for x in range (179):
            for y in range (37):
                card = []
                if ((M.z[y][x: x+1] == ".") and (M.Ns[y][x] == -1)):
                    try:
                        if M.Ns[max(0, y-1)][x] == n:
                            M.Ns[y][x] = n + 1
                    except: continue
                    try:
                        if M.Ns[y+1][x] == n:
                            M.Ns[y][x] = n + 1
                    except: continue
                    try:
                        if M.Ns[y][max(0, x-1)] == n:
                            M.Ns[y][x] = n + 1
                    except: continue
                    try:
                        if M.Ns[y][x+1] == n:
                            M.Ns[y][x] = n + 1
                    except: continue

def find_shortest():
    ds = []
    for i in range (8):
        ds.append([0] * 8)

    for p1 in range (8):
        clear(); M.Ns[M.P[p1][1]][M.P[p1][0]] = 0
        find_route()
        for p2 in range (8):
            ds[p1][p2] = M.Ns[M.P[p2][1]][M.P[p2][0]]
            print "%i - %i:" % (p1, p2), ds[p1][p2], "\b,"
        print ""

    for p2 in range (1, 8):
        for p3 in range (1, 8):
            if p3 != p2:
                for p4 in range (1, 8):
                    if (p4 != p3) and (p4 != p2):
                        for p5 in range (1, 8):
                            if (p5 != p4) and (p5 != p3) and (p5 != p2):
                                for p6 in range (1, 8):
                                    if ((p6 != p5) and (p6 != p4) and
    (p6 != p3) and (p6 != p2)):
                                        for p7 in range (1, 8):
                                            if ((p7 != p6) and
    (p7 != p5) and (p7 != p4) and (p7 != p3) and (p7 != p2)):
                                                for p8 in range (1, 8):
                                                    if (
    (p8 != p7) and (p8 != p6) and (p8 != p5) and (p8 != p4) and
    (p8 != p3) and (p8 != p2)):
                                                        M.Rs.append(
    "0%i%i%i%i%i%i%i0" % (p2, p3, p4, p5, p6, p7, p8))
                                                        M.Ds.append(
    ds[0][p2] + ds[p2][p3] + ds[p3][p4] + ds[p4][p5] +
    ds[p5][p6] + ds[p6][p7] + ds[p7][p8] + ds[p8][0])
                                                        print (
    M.Rs[-1], M.Ds[-1])

    print min (M.Ds)

#######################################################################
# Main Routine
print ""
load()
for m in range (len(M.z)):
    print " " + M.z[m]
print ""
print M.P
print ""
find_shortest()
print "\n"
