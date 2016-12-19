#######################################################################
# Setup
class Data(object):
    def __init__(self):
        self.ata = "10111011111001111"
D = Data()

#######################################################################
#
def frac(data):
    flip = ""
    for i in range (len(data)):
        flip = str(int(not int(data[i: i+1]))) + flip
    data = data + "0" + flip
    return data

def fill_disk(data, L):
    while len(data) < L: data = frac(data)
    data = data[: L]
    return data

def check1(S):
    C = ""
    for i in range (len(S) / 2):
        if S[2*i: 2*i + 1] == S[2*i + 1: 2*(i+1)]: C = C + "1"
        else: C = C + "0"
    return C

def checksum(data):
    C = check1(data)
    while ((len(C) % 2) == 0):
        C = check1(C)
    return C

#######################################################################
# Main Routine
print ""
# d = fill_disk("10000", 20); print d
d = fill_disk(D.ata, 272); print d
c = checksum(d); print c
print "\n"
