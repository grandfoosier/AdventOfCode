class Sequence(object):
    def __init__(self):
        self.I = ""
S = Sequence()

fname = "AoC_09_1.txt"
S.I = [line.rstrip('\n') for line in open(fname)][0]
print "\nSequence Loaded\n\n"

def decompress(SI, I):
    pl = SI.find("("); SF = 0; print ""
    while pl >= 0:
        SF += len (SI[: pl]); SI = SI[pl: ]

        x = SI.find("x"); pr = SI.find(")")
        A = int(SI[1: x]); B = int(SI[x + 1: pr])
        SI = SI[pr + 1: ]
        print ("    " * I), "\b[%ix%i]" % (A, B), SI[: A]
        SF += (decompress(SI[: A], I + 1) * B); SI = SI[A: ]

        pl = SI.find("(")

    SF += len(SI[: ]); SI = ""

    return SF

L = decompress(S.I, 0); print "\n-----", L, "-----"

print "\n"
