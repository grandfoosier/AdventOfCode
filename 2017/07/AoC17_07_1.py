fname = "AoC17_07_1.txt"
diags = [line for line in open(fname)]
print "\nDiagnostics Opened\n"

suprs = {}; w8ts = {}

for l in diags:
    prgm = l[: l.find(" ")]

    w = int(l[l.find("(")+1: l.find(")")])
    w8ts[prgm] = w

    arw = l.find(">")
    if arw > 0: subs = l[arw +2: -1].replace(",","").split()
    else: subs = []

    for s in subs:
        suprs[s] = prgm
print "Diagnostics Loaded\n"

print set(w8ts) - set(suprs)
print "\n"
