fname = "AoC_07_1.txt"
IPAs = [line.rstrip('\n') for line in open(fname)]
print "\nAddresses Opened"

class Sequence_list(object):
    def __init__(self):
        self.Ys = []; self.Ns = []
S = Sequence_list()

for i in range (len(IPAs)):
# for i in range (20):
    b_l = IPAs[i].find("["); b_r = IPAs[i].find("]")

    S.Ys.append([IPAs[i][: b_l]])
    S.Ns.append([IPAs[i][b_l + 1: b_r]])
    IPAs[i] = IPAs[i][b_r + 1: ]

    b_l = IPAs[i].find("["); b_r = IPAs[i].find("]")
    while b_l > 0:
        S.Ys[i].append(IPAs[i][: b_l])
        S.Ns[i].append(IPAs[i][b_l + 1: b_r])
        IPAs[i] = IPAs[i][b_r + 1: ]
        b_l = IPAs[i].find("["); b_r = IPAs[i].find("]")

    S.Ys[i].append(IPAs[i][b_r + 1: ])

print "Addresses Uploaded."

def ABA_check(s, l):
    for i in range (len(s) - 2):
        if ((s[i + 0] == s[i + 2]) and
            (s[i + 0] != s[i + 1])):
            l.append(s[i: i + 3])

def SSL_check(i):
    S.ABAs = []; S.BABs = []
    for j in range (len(S.Ns[i])):
        ABA_check(S.Ns[i][j], S.BABs)
        print "(-)", S.Ns[i][j]
    print S.BABs
    for j in range (len(S.Ys[i])):
        ABA_check(S.Ys[i][j], S.ABAs)
        print S.Ys[i][j]
    print S.ABAs

    for x in range (len(S.ABAs)):
        BAB = S.ABAs[x][1] + S.ABAs[x][0] + S.ABAs[x][1]
        if BAB in S.BABs: return True
    return False

print ""
SSL = 0
for i in range (len(S.Ys)):
    if SSL_check(i): SSL += 1
    print " " * 80, SSL
print "\n"
