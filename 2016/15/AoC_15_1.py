#######################################################################
# Setup
class Disks(object):
    def __init__(self):
        self.t = 0; self.s = [0, 0, 2, 2, 0, 7]
    def adv(self):
        for i in range (6): self.s[i] += 1
    def rot(self):
        self.s[0] = self.s[0] % 7;  self.s[1] = self.s[1] % 13
        self.s[2] = self.s[2] % 3;  self.s[3] = self.s[3] % 5
        self.s[4] = self.s[4] % 17; self.s[5] = self.s[5] % 19
D = Disks()

#######################################################################
# Loading
def prep():
    for i in range (6): D.s[i] += (i + 1)
    D.rot()

#######################################################################
#
def first_capsule():
    while sum(D.s) != 0:
        D.t += 1; D.adv(); D.rot()

#######################################################################
# Main Routine
print ""
prep()
first_capsule()
print D.t, D.s
print "\n"
