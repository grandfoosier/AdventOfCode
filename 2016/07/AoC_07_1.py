fname = "AoC_07_1.txt"
IPAs = [line.rstrip('\n') for line in open(fname)]
print "\nAddresses Opened"

class Sequence_list(object):
    def __init__(self):
        self.Ys = []
        self.Ns = []
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

def ABBA_check(s):
    for i in range (len(s) - 3):
        if ((s[i + 0] == s[i + 3]) and
            (s[i + 1] == s[i + 2]) and
            (s[i + 0] != s[i + 1])):
            return True
    return False

def TLS_check(i):
    for j in range (len(S.Ns[i])):
        print "(-)", S.Ns[i][j], ABBA_check(S.Ns[i][j])
        if ABBA_check(S.Ns[i][j]): return False
    for j in range (len(S.Ys[i])):
        print S.Ys[i][j], ABBA_check(S.Ys[i][j])
        if ABBA_check(S.Ys[i][j]): return True
    return False

print ""

TLS = 0
for i in range (len(S.Ys)):
    if TLS_check(i): TLS += 1
    print " " * 40, TLS

print "\n"
