class Sequence(object):
    def __init__(self):
        self.I = ""; self.F = ""
S = Sequence()

fname = "AoC_09_1.txt"
S.I = [line.rstrip('\n') for line in open(fname)][0]
print "\nSequence Loaded\n\n"

def decompress():
    pl = S.I.find("(")
    while pl >= 0:
        print S.I[: pl], "\n"
        S.F = S.F + S.I[: pl]; S.I = S.I[pl: ]

        x = S.I.find("x"); pr = S.I.find(")")
        A = int(S.I[1: x]); B = int(S.I[x + 1: pr])
        S.I = S.I[pr + 1: ]

        print "[%ix%i]" % (A, B), S.I[: A]
        S.F = S.F + (S.I[: A] * B); S.I = S.I[A: ]
        pl = S.I.find("(")
        print "\n", pl, x, pr
        pause = raw_input("")

    S.F = S.F + S.I[: ]; S.I = ""

    L = len(S.F); print L

decompress()

print "\n"
