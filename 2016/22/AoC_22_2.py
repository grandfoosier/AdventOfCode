#######################################################################
#
class Nodes(object):
    def __init__(self):
        self.pos = []
        self.data = []
        self.free = []
        self.G = (0, 0)
        self.F = (0, 0)
        self.mv = 0
N = Nodes()

def load():
    fname = "AoC_22_1.txt"
    Ns = [line.rstrip('\n') for line in open(fname)]
    print "Node Info Opened\n"

    for i in range (2, len(Ns)):
        yind = Ns[i].find("y")
        N.pos.append((int(Ns[i][16: yind-1]),
                      int(Ns[i][yind+1: 22])))
        N.data.append([int(Ns[i][24: 27]),
                       int(Ns[i][30: 33])])

    N.G = (N.pos[-1][0], 0)
    print "Node Info Loaded\n"

def calc_free():
    N.free = []
    for i in range (len(N.data)):
        N.free.append(N.data[i][0] - N.data[i][1])
        assert N.free[i] > 0
        if N.data[i][1] == 0:
            N.F = (N.pos[i][0], N.pos[i][1])

def viable():
    V = 0
    for i in range (len(N.pos)):
        for j in range (len(N.pos)):
            if N.data[i][1] != 0:
                if i != j:
                    if N.data[i][1] <= N.free[j]: V += 1
    return V

def viable_n0():
    V = 0
    for i in range (len(N.pos)):
        for j in range (len(N.pos)):
            if N.data[i][1] != 0:
                if i != j:
                    if N.data[j][1] != 0:
                        if N.data[i][1] <= N.free[j]: V += 1
    return V

def print_L():
    Nx = N.pos[-1][0] + 1; Ny = N.pos[-1][1] + 1
    for y in range (Ny):
        for x in range (Nx):
            print str(N.data[y + Ny*x][1]) + "/" + str(N.data[y + Ny*x][0]),
        print "\n",

def print_S():
    Nx = N.pos[-1][0] + 1; Ny = N.pos[-1][1] + 1
    print "\n ",
    for y in range (Ny):
        for x in range (Nx):
            if x == y == 0:
                if N.G == (x, y): print "\b(G)",
                elif N.data[y + Ny*x][1] > 50: print "\b(.)",
                elif N.data[y + Ny*x][1] > 0: print "\b(u)",
                else: print "\b(_)",

            elif N.data[y + Ny*x][0] < 100:
                if N.G == (x, y): print "\b G ",
                elif N.data[y + Ny*x][1] > 50: print "\b . ",
                elif N.data[y + Ny*x][1] > 0: print "\b u ",
                else: print "\b _ ",
            else:
                if N.data[y + Ny*x][1] > 100: print "\b X ",
                elif N.data[y + Ny*x][1] > 50: print "\b . ",
                elif N.data[y + Ny*x][1] > 0: print "\b u ",
                else: print "\b _ ",
        print "\n ",

def move_open():
    for i in range (12):
        (x, y) = N.F
        tomove = N.data[N.pos.index((x-1, y))][1]
        N.data[N.pos.index((x, y))][1] = tomove
        N.data[N.pos.index((x-1, y))][1] = 0
        N.mv += 1
        calc_free()

    for i in range (29):
        (x, y) = N.F
        tomove = N.data[N.pos.index((x, y-1))][1]
        N.data[N.pos.index((x, y))][1] = tomove
        N.data[N.pos.index((x, y-1))][1] = 0
        N.mv += 1
        calc_free()

    for i in range (28):
        (x, y) = N.F
        tomove = N.data[N.pos.index((x+1, y))][1]
        N.data[N.pos.index((x, y))][1] = tomove
        N.data[N.pos.index((x+1, y))][1] = 0
        N.mv += 1
        calc_free()

    for i in range (31):
        (x, y) = N.F
        tomove = N.data[N.pos.index((x+1, y))][1]
        N.data[N.pos.index((x, y))][1] = tomove
        N.data[N.pos.index((x+1, y))][1] = 0
        N.mv += 1
        calc_free()
        N.G = ((x, y))

        (x, y) = N.F
        tomove = N.data[N.pos.index((x, y+1))][1]
        N.data[N.pos.index((x, y))][1] = tomove
        N.data[N.pos.index((x, y+1))][1] = 0
        N.mv += 1
        calc_free()

        (x, y) = N.F
        tomove = N.data[N.pos.index((x-1, y))][1]
        N.data[N.pos.index((x, y))][1] = tomove
        N.data[N.pos.index((x-1, y))][1] = 0
        N.mv += 1
        calc_free()

        (x, y) = N.F
        tomove = N.data[N.pos.index((x-1, y))][1]
        N.data[N.pos.index((x, y))][1] = tomove
        N.data[N.pos.index((x-1, y))][1] = 0
        N.mv += 1
        calc_free()

        (x, y) = N.F
        tomove = N.data[N.pos.index((x, y-1))][1]
        N.data[N.pos.index((x, y))][1] = tomove
        N.data[N.pos.index((x, y-1))][1] = 0
        N.mv += 1
        calc_free()

    (x, y) = N.F
    tomove = N.data[N.pos.index((x+1, y))][1]
    N.data[N.pos.index((x, y))][1] = tomove
    N.data[N.pos.index((x+1, y))][1] = 0
    N.mv += 1
    calc_free()
    N.G = ((x, y))
    print_S()
    print N.mv
    pause = raw_input("")

#######################################################################
# Main Routine
print ""

load(); calc_free()
# print viable()
# print viable_n0()
# print_L()
print_S()
move_open()

print "\n"
