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
Me = You()

def go(turn, N):
    print Me.D, Me.x, Me.y
    print turn, N

    if turn == "R": Me.D = Me.compass[
        (Me.compass.index(Me.D) + 1) % 4]
    else: Me.D = Me.compass[(Me.compass.index(Me.D) - 1) % 4]

    print Me.D,

    if   Me.D == "N": Me.y += N
    elif Me.D == "S": Me.y -= N
    elif Me.D == "E": Me.x += N
    else:             Me.x -= N

    print Me.x, Me.y

for d in dirs:
    go(d[: 1], int(d[1: ]))
    print ""

L = abs(Me.x) + abs(Me.y)
print L
