fname = "AoC17_09_1.txt"
S = [line for line in open(fname)][0].rstrip("\n")
print "\nStream Opened\n"

while True:
    x = S.find("!")
    if x < 0: break
    else: S = S[:x] + S[x+2:]
print "Stream Organized\n"

G = ""
while True:
    x = S.find("<")
    if x < 0: break
    else:
        y = S[x:].find(">") + x
        G = G + S[x+1: y]
        S = S[:x] + S[y+1:]
print "Stream Cleaned\n"

print len(G)
print "\n"
