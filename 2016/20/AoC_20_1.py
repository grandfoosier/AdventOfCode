#######################################################################
#
def U_of_M(M_all, M_add):
    M_all.append(M_add)
    i = 0; j = 1
    while i < (len(M_all) - 1):
        while j < (len(M_all)):
            (a, b) = M_all[i]
            (x, y) = M_all[j]
            if (((a - 2) < x < (b + 2)) or
                ((a - 2) < y < (b + 2))):
                M_all[i] = (min(a, x), max(b, y))
                del M_all[j]
                i = 0; j = 0
            j += 1
        i += 1; j = i + 1
    return sorted(M_all)

def load():
    fname = "AoC_20_1.txt"
    IPs = [line.rstrip('\n') for line in open(fname)]
    print "Blocked IPs Opened\n"

    M_all = []
    hyph = IPs[0].find("-")
    M_all.append((int(IPs[0][: hyph]), int(IPs[0][hyph + 1: ])))
    print M_all[0]

    for i in range (1, len(IPs)):
        hyph = IPs[i].find("-")
        M_add = (int(IPs[i][: hyph]), int(IPs[i][hyph + 1: ]))
        print M_add
        M_all = U_of_M(M_all, M_add)
    print "\nBlocked IPs Loaded\n"
    return M_all

#######################################################################
# Main Routine
print ""

M_all = load(); print "\n", M_all, "\n"
(a, b) = M_all[0]
if a == 0: print b + 1
else: print 0

print "\n"
