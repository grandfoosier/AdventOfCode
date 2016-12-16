#######################################################################
# Setup
class Maze(object):
    def __init__(self):
        self.z = ["?" * 50] * 50
        # self.z[1] = self.z[1][: 1] + "S" + self.z[1][2: ]
        # self.z[39] = self.z[39][: 31] + "F" + self.z[39][32: ]
        self.Ns = []
        for i in range (50): self.Ns.append([])
        for i in range (50):
            for j in range (50): self.Ns[i].append(-1)
        self.Ns[1][1] = 0
M = Maze()

#######################################################################
#
def wyn(x, y):
    Z = x*x + 3*x + 2*x*y + y + y*y
    Z += 1364
    Z = format(Z, 'b')
    s = 0
    for i in range (len(Z)):
        s += int(Z[i: i+1])
    if s % 2: return "#"
    else: return "."

def fill_maze():
    for x in range (0, 50):
        for y in range (0, 50):
            M.z[y] = M.z[y][: x] + wyn(x, y) + M.z[y][x+1: ]
    M.z[1] = M.z[1][: 1] + "S" + M.z[1][2: ]
    # M.z[39] = M.z[39][: 31] + "F" + M.z[39][32: ]

def find_route():
    for n in range (100):
        for x in range (50):
            for y in range (50):
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

#######################################################################
# Main Routine
print ""
fill_maze()
for m in range (len(M.z)):
    print "  " + M.z[m]
print ""
find_route()
for m in range (len(M.Ns)):
    print M.Ns[m]
print ""
print M.Ns[39][31]
print "\n"
