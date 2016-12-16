#######################################################################
# Setup
class Register(object):
    def __init__(self):
        self.v = 0
A = Register(); B = Register(); C = Register(); D = Register();
C.v = 1

class Instructions(object):
    def __init__(self):
        self.s = []
        self.N = 0
        self.l = ["a", "b", "c", "d"]
        self.m = [A, B, C, D]
I = Instructions()

#######################################################################
# Loading
fname = "AoC_12_1.txt"
Is = [line.rstrip('\n') for line in open(fname)]
print "\nInstructions Opened\n"

for i in Is:
    if i[: 3] == "cpy":
        sp2 = i[4: ].find(" ") + 4
        I.s.append(["cpy", i[4: sp2], i[sp2 + 1: ]])
    elif i[: 3] == "inc":
        I.s.append(["inc", i[4: ]])
    elif i[: 3] == "dec":
        I.s.append(["dec", i[4: ]])
    else:
        sp2 = i[4: ].find(" ") + 4
        I.s.append(["jnz", i[4: sp2], int(i[sp2 + 1: ])])

print "Instructions Loaded\n"

#######################################################################
#
def read_instructions():
    inst = I.s[I.N]
    if inst[0] == "cpy":
        try: what = int(inst[1])
        except: what = I.m[I.l.index(inst[1])].v
        I.m[I.l.index(inst[2])].v = what; I.N += 1
    elif inst[0] == "inc":
        I.m[I.l.index(inst[1])].v += 1; I.N += 1
    elif inst[0] == "dec":
        I.m[I.l.index(inst[1])].v -= 1; I.N += 1
    else:
        try: what = int(inst[1])
        except: what = I.m[I.l.index(inst[1])].v
        if what > 0: I.N += inst[2]
        else:
            print "\rA:", A.v, "B:", B.v, "C:", C.v, "D:", D.v, I.s[I.N],
            I.N += 1

#######################################################################
# Main Routine
print "\rA:", A.v, "B:", B.v, "C:", C.v, "D:", D.v, I.s[I.N],
while I.N < len(I.s):
    read_instructions()
print "\n\n"
