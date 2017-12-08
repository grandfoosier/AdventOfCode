fname = "AoC17_08_1.txt"
Is = [line for line in open(fname)]
print "\nDiagnostics Opened\n"

Rs = {}

def read_L(L):
    r1 = L[: L.find(" ")]
    L = L[L.find(" ")+1:]

    o1 = L[: L.find(" ")]
    L = L[L.find(" ")+1:]

    n1 = int(L[: L.find(" ")])
    L = L[L.find(" ")+4:]

    r2 = L[: L.find(" ")]
    L = L[L.find(" ")+1:]

    o2 = L[: L.find(" ")]
    L = L[L.find(" ")+1:]

    n2 = int(L[: L.find("\n")])

    try: x = Rs[r1]
    except: Rs[r1] = 0

    try: x = Rs[r2]
    except: Rs[r2] = 0

    if   o1 == "inc": m =  1
    elif o1 == "dec": m = -1

    if   o2 == "<" : chk = Rs[r2] <  n2
    elif o2 == "<=": chk = Rs[r2] <= n2
    elif o2 == ">" : chk = Rs[r2] >  n2
    elif o2 == ">=": chk = Rs[r2] >= n2
    elif o2 == "==": chk = Rs[r2] == n2
    elif o2 == "!=": chk = Rs[r2] != n2

    if chk: Rs[r1] += (n1 * m)

for I in Is:
    read_L(I)

print max(Rs.values())
print "\n"
