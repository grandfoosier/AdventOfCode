from hashlib import md5

#######################################################################
# Setup
class Map(object):
    def __init__(self):
        self.p = []
M = Map()

#######################################################################
#
def find_next(lst):
    lst = "." + lst + "."; nxt = ""
    for i in range (1, len(lst) - 1):
        if lst[i-1] == lst[i+1]: nxt = nxt + "."
        else: nxt = nxt + "^"
    return nxt

def count_safes(row):
    s = 0
    for j in range (len(row)):
        if row[j] == ".": s += 1
    return s

def count_iter(L, row):
    s = count_safes(row)
    for i in range (L - 1):
        row = find_next(row)
        s += count_safes(row)
    return s

#######################################################################
# Main Routine
print ""
# safes = count_iter(3, "..^^.");
# safes = count_iter(10, ".^^.^.^^^^");
# safes = count_iter(40, ".^.^..^......^^^^^...^^^." +
#                        "..^...^....^^.^...^.^^^^." +
#                        "...^...^^.^^^...^^^^.^^.^" +
#                        ".^^..^.^^^..^^^^^^.^^^..^");
safes = count_iter(400000, ".^.^..^......^^^^^...^^^." +
                           "..^...^....^^.^...^.^^^^." +
                           "...^...^^.^^^...^^^^.^^.^" +
                           ".^^..^.^^^..^^^^^^.^^^..^");

print "\n", safes, "safe tiles"

print "\n"
