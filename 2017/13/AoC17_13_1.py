fname = "AoC17_13_1.txt"
Walls = [line.rstrip("\n") for line in open(fname)]
print "\nFirewall Opened\n"

Rs = {}; Ss = {}; Ps = {}
for w in Walls:
    d = int(w[: w.find(":")])
    r = int(w[w.find(" ")+1:]) - 1
    Rs[d] = r; Ss[d] = 0; Ps[d] = 1
print "Firewall Loaded\n"

def advance():
    for d in Ss.keys():
        Ss[d] += Ps[d]
        if Ss[d] == Rs[d]: Ps[d] = -1
        elif Ss[d] == 0: Ps[d] = 1

def disp(t):
    for j in range(max(Rs.values())):
        for i in range(max(Rs.keys())+1):
            try:
                if t == i and Ss[i] == 0 and j == 0: print "X",
                elif t == i and j == 0: print "=",
                elif Ss[i] == j: print "O",
                elif j <= Rs[i]: print ":",
                else: print " ",
            except:
                if t == i and j == 0: print "=",
                else: print " ",
        print ""

s = 0
for t in range(max(Ss.keys())+1):
    # disp(t)
    try:
        if Ss[t] == 0:
            # print "%i + (%i * %i) = %i" % (
            #     s, t, Rs[t]+1, s+t*(Rs[t]+1))
            s += t * (Rs[t] + 1)
    except: pass
    # p = raw_input("")
    advance()

print "Severity:", s
print "\n"
