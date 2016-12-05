fname = "AoC_03_1.txt"
onwall = [line.rstrip('\n') for line in open(fname)]
print "Triads Opened"
Ts = []

for t in range (len(onwall)):
    Ts.append(sorted([int(onwall[t][ 2:  5]),
                      int(onwall[t][ 7: 10]),
                      int(onwall[t][12: 15])]))
print "Triads Uploaded."

class You(object):
    def __init__(self):
        self.OK = 0
Me = You()

for t in Ts:
    if t[0] + t[1] > t[2]: Me.OK += 1

print Me.OK, "triangles are possible."
print "\n"
