from hashlib import md5

#######################################################################
# Setup
class Path(object):
    def __init__(self):
        self.Ns = []
        self.Ps = []
P = Path()

#######################################################################
#
def find_open(code, path, x, y):
    h = md5(code + path).hexdigest()
    O = []
    for i in range (4):
        if int(h[i], 16) > 10: O.append(1)
        else: O.append(0)

    if x == 0: O[2] = 0
    if x == 3: O[3] = 0
    if y == 0: O[0] = 0
    if y == 3: O[1] = 0

    return O

def find_all(code, path, x, y, N):
    if x == y == 3:
        P.Ns.append(N)
        P.Ps.append(path)
        return 1

    # if len(P.Ns) > 0:
    #     if N >= min(P.Ns): return 0

    O = find_open(code, path, x, y)

    if O[1]: find_all(code, path + "D", x, y + 1, N + 1)
    if O[3]: find_all(code, path + "R", x + 1, y, N + 1)
    if O[0]: find_all(code, path + "U", x, y - 1, N + 1)
    if O[2]: find_all(code, path + "L", x - 1, y, N + 1)

#######################################################################
# Main Routine
print ""
# find_all("ihgpwlah", "", 0, 0, 0)
# find_all("kglvqrro", "", 0, 0, 0)
# find_all("ulqzkmiv", "", 0, 0, 0)
find_all("hhhxzeay", "", 0, 0, 0)
if len(P.Ns) > 0:
    N = P.Ns.index(max(P.Ns))
    print P.Ns[N], P.Ps[N]
else:
    print "No paths found"
print "\n"
