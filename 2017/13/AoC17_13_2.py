fname = "AoC17_13_1.txt"
Walls = [line.rstrip("\n") for line in open(fname)]
# Walls = ["0: 3","1: 2","4: 4","6: 4"]
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

def advance1(d):
    for i in range(d):
        Ss[d] += Ps[d]
        if Ss[d] == Rs[d]: Ps[d] = -1
        elif Ss[d] == 0: Ps[d] = 1

def disp(t):
    for j in range(max(Rs.values())+1):
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

for d in range(max(Ss.keys())+1):
    try:
        r = Rs[d]
        advance1(d)
    except: pass

t = 0
while True:
    if (t / 10000) == (t * 1.0 / 10000):
        print "\rElapsed: %.3g us   " % (t * 1.0 / 1000000),
    if 0 not in Ss.values(): break
    advance()
    t += 1

# disp(0)
print "\n\nTime:", t, "ps"
print "\n"
