fname = "AoC17_12_1.txt"
Connections = [line.rstrip("\n") for line in open(fname)]
print "\nConnections Opened\n"

Cs = {}
for c in Connections:
    s = c.find(" "); r = c.find(">")
    N = int(c[:s])
    P = set(map(int, c[r+2:].split(", ")))
    Cs[N] = P
print "Connections Loaded\n"

Js = {0:[0]}; i = 0; X = set([0])
while True:
    l = Js[i]
    print "%i:" % i, Js[i]

    a = set()
    for m in l: a |= Cs[m]
    a -= X
    if len(a) == 0: break

    Js[i+1] = list(sorted(a))
    X |= a; i += 1

print ""
print "Programs in group 0:", len(X)
print "\n"
