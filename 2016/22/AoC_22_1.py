#######################################################################
#
class Nodes(object):
    def __init__(self):
        self.pos = []
        self.data = []
        self.free = []
N = Nodes()

def load():
    fname = "AoC_22_1.txt"
    Ns = [line.rstrip('\n') for line in open(fname)]
    print "Node Info Opened\n"

    for i in range (2, len(Ns)):
        yind = Ns[i].find("y")
        N.pos.append((int(Ns[i][16: yind-1]),
                      int(Ns[i][yind+1: 22])))
        N.data.append((int(Ns[i][24: 27]),
                       int(Ns[i][30: 33])))
    print "Node Info Loaded\n"

def calc_free():
    N.free = []
    for i in range (len(N.data)):
        N.free.append(N.data[i][0] - N.data[i][1])

def viable():
    V = 0
    for i in range (len(N.pos)):
        for j in range (len(N.pos)):
            if N.data[i][1] != 0:
                if i != j:
                    if N.data[i][1] <= N.free[j]: V += 1
    return V

#######################################################################
# Main Routine
print ""

load(); calc_free()
print viable()

print "\n"
