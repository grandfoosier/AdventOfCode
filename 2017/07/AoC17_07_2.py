fname = "AoC17_07_1.txt"
diags = [line for line in open(fname)]
print "\nDiagnostics Opened\n"

suprs = {}; w8ts = {}; twrs = {}

for l in diags:
    prgm = l[: l.find(" ")]

    w = int(l[l.find("(")+1: l.find(")")])
    w8ts[prgm] = w

    arw = l.find(">")
    if arw > 0: subs = l[arw +2: -1].replace(",","").split()
    else: subs = []
    twrs[prgm] = subs

    for s in subs:
        suprs[s] = prgm
print "Diagnostics Loaded\n"

def tower_weight(p):
    if len(twrs[p]) == 0: return w8ts[p]

    next_twrs = []
    next_twr_ws = []
    for t in twrs[p]:
        next_twrs.append(t)
        next_twr_ws.append(tower_weight(t))

    if min(next_twr_ws) < max(next_twr_ws):
        tempW = next_twr_ws[:]; tempP = next_twrs[:]
        wL = min(tempW)
        pL = tempP[tempW.index(wL)]
        del(tempW[tempW.index(wL)])
        del(tempP[tempP.index(pL)])

        wU = max(tempW)
        pU = tempP[tempW.index(wU)]
        del(tempW[tempW.index(wU)])
        del(tempP[tempP.index(pU)])

        if min(tempW) == wL:
            print "Program \"%s\" has the wrong weight (%i)" % (
                pU, w8ts[pU])
            print " -it should be %i" % (w8ts[pU] - wU + wL)
            return w8ts[p] + wL * len(next_twrs)
        else:
            print "Program \"%s\" has the wrong weight (%i)" % (
                pL, w8ts[pL])
            print " -it should be %i" % (w8ts[pL] + wU - wL)
            return w8ts[p] + wU * len(next_twrs)

    return w8ts[p] + sum(next_twr_ws)

top = list(set(w8ts) - set(suprs))[0]

T = tower_weight(top)
print "\n"
