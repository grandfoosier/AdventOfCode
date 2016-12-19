from hashlib import md5

#######################################################################
# Setup
class Map(object):
    def __init__(self):
        self.p = []
M = Map()

#######################################################################
#
def find_next():
    lst = "." + M.p[-1] + "."; nxt = ""
    for i in range (1, len(M.p[-1]) + 1):
        if lst[i-1] == lst[i+1]: nxt = nxt + "."
        else: nxt = nxt + "^"
    return nxt

def make_map(L, frst):
    M.p.append(frst);
    for i in range (L - 1): M.p.append(find_next())

    for m in range (len(M.p)): print M.p[m]

def count_safe():
    s = 0
    for i in range (len(M.p)):
        for j in range (len(M.p[i])):
            if M.p[i][j] == ".": s += 1
    return s

#######################################################################
# Main Routine
print ""
# make_map(3, "..^^.");
# make_map(10, ".^^.^.^^^^");
make_map(40, ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^." +
             "...^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^");

print "\n", count_safe(), "safe tiles"

print "\n"
