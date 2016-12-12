#######################################################################
# Setup
class Bots(object):
    def __init__(self):
        self.inv = []
        for i in range (210): self.inv.append([])
        self.send = []
        for i in range (210): self.send.append([])
B = Bots()

class Outputs(object):
    def __init__(self):
        self.inv = []
        for i in range (21): self.inv.append([])
O = Outputs()

class Comparisons(object):
    def __init__(self):
        self.mp = {}
C = Comparisons()

#######################################################################
# Loading
fname = "AoC_10_1.txt"
I = [line.rstrip('\n') for line in open(fname)]
print "\nInstructions Opened\n"

for i in I:
    if i[: 3] == "bot":
        i_s1 = i.find(" ")
        i_s2 = i[i_s1 + 1: ].find(" ") + i_s1 + 1
        N = int(i[i_s1 + 1: i_s2])

        i_to1 = i.find("to")
        i_and = i.find("and")
        low_to = i[i_to1 + 3: i_and]
        if low_to[: 3] == "bot":
            B.send[N].append((B, int(low_to[4: ])))
        else:
            B.send[N].append((O, int(low_to[7: ])))

        i_to2 = i[i_and: ].find("to") + i_and
        high_to = i[i_to2 + 3: ]
        if high_to[: 3] == "bot":
            B.send[N].append((B, int(high_to[4: ])))
        else:
            B.send[N].append((O, int(high_to[7: ])))

    else:
        i_s1 = i.find(" ")
        i_s2 = i[i_s1 + 1: ].find(" ") + i_s1 + 1
        V = int(i[i_s1 + 1: i_s2])

        i_bot = i.find("bot")
        N = int(i[i_bot + 4: ])
        B.inv[N].append(V)
        B.inv[N] = sorted(B.inv[N])

print "Instructions Loaded\n"

#######################################################################
# Bot manager
def compare_and_distribute(N):
    C.mp[(B.inv[N][0], B.inv[N][1])] = N

    B.send[N][0][0].inv[B.send[N][0][1]].append(B.inv[N][0])
    B.send[N][0][0].inv[B.send[N][0][1]] = sorted(
        B.send[N][0][0].inv[B.send[N][0][1]])

    B.send[N][1][0].inv[B.send[N][1][1]].append(B.inv[N][1])
    B.send[N][1][0].inv[B.send[N][1][1]] = sorted(
        B.send[N][1][0].inv[B.send[N][1][1]])

    B.inv[N] = []

def holding_two():
    N = 0
    for x in B.inv:
        if len(x) == 2: return N
        N += 1
    return "X"

#######################################################################
# Main Routine
while True:
    N = holding_two()
    print "N:", N
    if N != "X":
        print "inv:", B.inv[N]
        print "send:", B.send[N]
        compare_and_distribute(N)
        print "inv:", B.inv[N]
        print ""
    else: break

print "\n"
print "comps:", C.mp
print "\n(17, 61):", C.mp[(17, 61)]
print "\n"
