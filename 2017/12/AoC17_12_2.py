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

def find_group(N):
    Js = {0:[N]}; i = 0; X = set([N])
    while True:
        l = Js[i]

        a = set()
        for m in l: a |= Cs[m]
        a -= X
        if len(a) == 0: break

        Js[i+1] = list(sorted(a))
        X |= a; i += 1
    return X

A = list(sorted(Cs.keys())); N = 0
print "Groups: ",
while True:
    i = A[0]; G = find_group(i); print i,
    A = list(sorted(set(A) - G)); N += 1
    if len(A) == 0: break

print "\n"
print "Number of groups:", N
print "\n"
