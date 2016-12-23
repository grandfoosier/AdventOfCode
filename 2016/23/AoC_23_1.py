#######################################################################
# Setup
class Register(object):
    def __init__(self):
        self.v = 0
A = Register(); B = Register(); C = Register(); D = Register();

class Instructions(object):
    def __init__(self):
        self.s = []
        self.N = 0
        self.l = ["a", "b", "c", "d"]
        self.m = [A, B, C, D]
I = Instructions()

#######################################################################
# Loading
fname = "AoC_23_1.txt"
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
    elif i[: 3] == "jnz":
        sp2 = i[4: ].find(" ") + 4
        I.s.append(["jnz", i[4: sp2], i[sp2 + 1: ]])
    elif i[: 3] == "tgl":
        I.s.append(["tgl", i[4: ]])

print "Instructions Loaded\n"

#######################################################################
#
def read_instructions():
    inst = I.s[I.N]
    if inst[0] == "cpy":
        try:
            try: what = int(inst[1])
            except: what = I.m[I.l.index(inst[1])].v
            I.m[I.l.index(inst[2])].v = what
        except: pass
    elif inst[0] == "inc":
        try: I.m[I.l.index(inst[1])].v += 1
        except: pass
    elif inst[0] == "dec":
        try: I.m[I.l.index(inst[1])].v -= 1
        except: pass
    elif inst[0] == "jnz":
        try:
            try: what = int(inst[1])
            except: what = I.m[I.l.index(inst[1])].v
            try: y = int(inst[2])
            except: y = I.m[I.l.index(inst[2])].v

            if what > 0: I.N += y - 1
            else:
                print "\rA:", A.v, "B:", B.v,
                print "C:", C.v, "D:", D.v, I.s[I.N],
        except: pass
    elif inst[0] == "tgl":
        try: x = int(inst[1])
        except: x = I.m[I.l.index(inst[1])].v

        X = I.N + x
        if X < len(I.s):
            if I.s[X][0] == "inc": I.s[X][0] = "dec"
            elif I.s[X][0] == "dec": I.s[X][0] = "inc"
            elif I.s[X][0] == "tgl": I.s[X][0] = "inc"
            elif I.s[X][0] == "cpy": I.s[X][0] = "jnz"
            elif I.s[X][0] == "jnz": I.s[X][0] = "cpy"

    I.N += 1

#######################################################################
# Main Routine
A.v = 7
print "\rA:", A.v, "B:", B.v, "C:", C.v, "D:", D.v, I.s[I.N],
while I.N < len(I.s):
    read_instructions()
print "\n\n"
