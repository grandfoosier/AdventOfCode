fname = "AoC_01_1.txt"
text = [line.rstrip('\n') for line in open(fname)][0]
print "Directions Opened"
dirs = []

while True:
    next_comma = text.find(",")
    if next_comma > 0:
        next_dir = text[0: next_comma]
        dirs.append(next_dir)
        text = text[next_comma + 2: ]
    else:
        dirs.append(text)
        print "Directions Uploaded."
        break

class You(object):
    def __init__(self):
        self.x = 0; self.y = 0; self.D = "N"
        self.compass = ["N", "E", "S", "W"]
        self.Ps = [(0, 0)]
        self.keep_going = True
Me = You()

def go(turn, N):
    print Me.D, Me.x, Me.y
    print turn, N

    if turn == "R": Me.D = Me.compass[
        (Me.compass.index(Me.D) + 1) % 4]
    else: Me.D = Me.compass[(Me.compass.index(Me.D) - 1) % 4]

    print Me.D,

    for n in range (N):
        if   Me.D == "N": Me.y += 1
        elif Me.D == "S": Me.y -= 1
        elif Me.D == "E": Me.x += 1
        else:             Me.x -= 1

        P = (Me.x, Me.y)
        if P in Me.Ps:
            Me.keep_going = False
            break
        else: Me.Ps.append(P)

    print Me.x, Me.y
    print ""

for d in dirs:
    if Me.keep_going: go(d[: 1], int(d[1: ]))
    else: break

print Me.D, Me.x, Me.y
L = abs(Me.x) + abs(Me.y)
print L
