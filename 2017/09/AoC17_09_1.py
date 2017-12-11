fname = "AoC17_09_1.txt"
S = [line for line in open(fname)][0].rstrip("\n")
print "\nStream Opened\n"

while True:
    x = S.find("!")
    if x < 0: break
    else: S = S[:x] + S[x+2:]
print "Stream Organized\n"

while True:
    x = S.find("<")
    if x < 0: break
    else:
        y = S[x:].find(">") + x
        S = (S[:x] + S[y+1:]).replace(",","")
print "Stream Cleaned\n"

L = 1; i = 0; T = 0
while i < len(S):
    if S[i] == "{":
        T += L
        if S[i+1] == "{": L += 1
        else: i += 1
    else: L -= 1
    i += 1
print T
print "\n"
