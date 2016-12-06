fname = "AoC_06_1.txt"
signals = [line.rstrip('\n') for line in open(fname)]
print "\nSignals Opened"
Ss = []
for i in range (8):
    Ss.append({"a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
               "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
               "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
               "q": 0, "r": 0, "s": 0, "t": 0, "u": 0,
               "v": 0, "w": 0, "x": 0, "y": 0, "z": 0})

for l in range (len(signals)):
    for i in range (8):
        Ss[i][signals[l][i: i + 1]] += 1
print "Signals Uploaded."

print ""

for i in range (8):
    n = max(Ss[i].values())

    temp = []
    for a in Ss[i]:
        if Ss[i][a] == n:
            temp.append(a)
            Ss[i][a] = 0
    stemp = sorted(temp)
    print stemp, "*", n

print "\n"
