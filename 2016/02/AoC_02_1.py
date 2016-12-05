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
        self.pos = [1, 1] # Y, X
        self.keypad = [["1", "2", "3"],
                       ["4", "5", "6"],
                       ["7", "8", "9"]]
Me = You()

def go(card):
    if card == "U": Me.pos[0] = max(0, Me.pos[0] - 1)
    if card == "D": Me.pos[0] = min(2, Me.pos[0] + 1)
    if card == "L": Me.pos[1] = max(0, Me.pos[1] - 1)
    if card == "R": Me.pos[1] = min(2, Me.pos[1] + 1)

for x in insx:
    for c in x:
        go(c)
    print "Next number is", Me.keypad[Me.pos[0]][Me.pos[1]]
    Me.psw += Me.keypad[Me.pos[0]][Me.pos[1]]

print Me.psw
print "\n"
