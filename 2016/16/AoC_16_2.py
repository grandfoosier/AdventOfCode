#######################################################################
# Setup
class Data(object):
    def __init__(self):
        self.ata = "10111011111001111"
D = Data()

#######################################################################
#
def frac0(data, x):
    flip = ""
    for i in range (len(data)):
        flip = str(int(not int(data[i: i+1]))) + flip
    data = data + x + flip + x
    return data

def fracn(data, x):
    m = len(data)/2
    flip = data[: m] + str(int(not int(data[m]))) + data[m+1: ]
    data = data + x + flip + x
    return data

def check1(S):
    C = ""
    for i in range (len(S) / 2):
        if S[2*i: 2*i + 1] == S[2*i + 1: 2*(i+1)]: C = C + "1"
        else: C = C + "0"
    return C[: -1], C[-1]

def frac_n_check(data, N):
    assert (len(data) % 2)
    data = frac0(data, "0"); print data
    data, x = check1(data); print data

    for i in range (N-1):
        data = fracn(data, x); print data
        data, x = check1(data); print data
    return data

#######################################################################
# Main Routine
print ""
N = 0
# L = 20
# L = 272
L = 35651584
while (L % 2 == 0):
    L /= 2; N += 1
print L, N
# d = frac_n_check("10000", N)
d = frac_n_check(D.ata, N)
print "\n"
