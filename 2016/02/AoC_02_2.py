fname = "AoC_02_1.txt"
dirs = [line.rstrip('\n') for line in open(fname)]
print "Instructions Opened"
insx = []

for d in range (len(dirs)):
    insx.append([])
    for x in range (len(dirs[d])):
        insx[d].append(dirs[d][0])
        dirs[d] = dirs[d][1: ]
print "Instructions Uploaded."

class You(object):
    def __init__(self):
        self.psw = ""
        self.pos = [0, -2] # Y, X
                      # -2   -1    0    1    2
        self.keypad = [["X", "X", "1"],           # -2
                       ["X", "2", "3", "4"],      # -1
                       ["5", "6", "7", "8", "9"], #  0
                       ["X", "A", "B", "C",],     #  1
                       ["X", "X", "D"]          ] #  2
Me = You()

def go(card):
    if card == "U":
        if ((abs(Me.pos[0]) + abs(Me.pos[1]) < 2) or
            (Me.pos[0] > 0)): Me.pos[0] -= 1
    if card == "D":
        if ((abs(Me.pos[0]) + abs(Me.pos[1]) < 2) or
            (Me.pos[0] < 0)): Me.pos[0] += 1
    if card == "L":
        if ((abs(Me.pos[0]) + abs(Me.pos[1]) < 2) or
            (Me.pos[1] > 0)): Me.pos[1] -= 1
    if card == "R":
        if ((abs(Me.pos[0]) + abs(Me.pos[1]) < 2) or
            (Me.pos[1] < 0)): Me.pos[1] += 1

for x in insx:
    for c in x:
        go(c)
    print "Next button is", Me.keypad[Me.pos[0] + 2][Me.pos[1] + 2]
    Me.psw += Me.keypad[Me.pos[0] + 2][Me.pos[1] + 2]

print Me.psw
print "\n"
