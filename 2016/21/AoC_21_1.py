#######################################################################
#
def swap_p(text, X, Y):
    print "swap pos", X, Y
    if X > Y: Y, X = X, Y

    x = text[X]; y = text[Y]
    text = text[: X] + y + text[X + 1: Y] + x + text[Y + 1:]
    print text, "\n"; return text

def swap_l(text, x, y):
    print "swap letter", x, y
    X = text.find(x); Y = text.find(y)
    text = swap_p(text, X, Y)
    return text

def rot_l(text, X):
    print "rot l", X
    for x in range (X): text = text[1: ] + text[0]
    print text, "\n"; return text

def rot_r(text, X):
    print "rot r", X
    for x in range (X): text = text[-1] + text[0: -1]
    print text, "\n"; return text

def rot_b(text, x):
    print "rot based on", x
    X = text.find(x)
    if X >= 4: X += 1
    text = rot_r(text, X + 1)
    return text

def rev(text, X, Y):
    print "reverse", X, Y
    if X > Y: Y, X = X, Y

    flipped = text[X: Y + 1][:: -1]
    text = text[: X] + text[X: Y + 1][:: -1] + text[Y + 1: ]
    print text, "\n"; return text

def move(text, X, Y):
    print "move", X, Y
    x = text[X]
    text = text[: X] + text[X + 1: ]
    text = text[: Y] + x + text[Y: ]
    print text, "\n"; return text

def load():
    fname = "AoC_21_1.txt"
    Fs = [line.rstrip('\n') for line in open(fname)]
    print "Scrambling Function Loaded\n"
    return Fs

def scramble(text, Fs):
    for i in range (len(Fs)):
        if   Fs[i][: 6] == "swap p":
            X = int(Fs[i][14])
            Y = int(Fs[i][-1])
            text = swap_p(text, X, Y)
        elif Fs[i][: 6] == "swap l":
            X = Fs[i][12]
            Y = Fs[i][-1]
            text = swap_l(text, X, Y)
        elif Fs[i][: 8] == "rotate l":
            X = int(Fs[i][12])
            text = rot_l(text, X)
        elif Fs[i][: 8] == "rotate r":
            X = int(Fs[i][13])
            text = rot_r(text, X)
        elif Fs[i][: 8] == "rotate b":
            X = Fs[i][-1]
            text = rot_b(text, X)
        elif Fs[i][: 7] == "reverse":
            X = int(Fs[i][18])
            Y = int(Fs[i][-1])
            text = rev(text, X, Y)
        elif Fs[i][: 4] == "move":
            X = int(Fs[i][14])
            Y = int(Fs[i][-1])
            text = move(text, X, Y)

#######################################################################
# Main Routine
print ""

Fs = load()
text = "abcdefgh"; print text, "\n"
text = scramble(text, Fs)

print "\n"
