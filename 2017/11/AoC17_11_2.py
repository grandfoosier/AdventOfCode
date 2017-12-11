fname = "AoC17_11_1.txt"
Steps = [line.rstrip("\n").split(",") for line in open(fname)][0]
print "\nSteps Loaded\n"

x,y = 0,0
Ds = []
for s in Steps:
    if s == "nw":
        x -= 1; y += 1
    elif s == "n": y += 1
    elif s == "sw": x -= 1
    elif s == "ne": x += 1
    elif s == "s": y -= 1
    elif s == "se":
        x += 1; y -= 1
    Ds.append(abs(x+y))

print max(Ds)
print "\n"
