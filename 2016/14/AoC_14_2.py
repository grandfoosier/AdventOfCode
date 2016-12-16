from hashlib import md5

#######################################################################
# Setup
class Keys(object):
    def __init__(self):
        self.eys = []
        self.Hs = []
        self.M3 = []
        self.M5 = []
        self.s = "ahsbgdzn"
        # self.s = "abc"
K = Keys()

#######################################################################
#
def hash_stretch(I):
    h = md5(K.s + str(I)).hexdigest()
    for i in range (0, 2016):
        h = md5(h).hexdigest()
    K.Hs.append(h)

    m1 = []
    for i in range (len(h) - 2):
        if h[i: i+3] == h[i] * 3:
            m1.append(h[i])
            break
    K.M3.append(m1)

    ms = []
    for i in range (len(h) - 4):
        if h[i: i+5] == h[i] * 5:
            if h[i] not in ms:
                ms.append(h[i])
    K.M5.append(ms)

def check_for_3(I):
    if len(K.M3[I]) == 1: return K.M3[I][0]
    return "g"

def check_for_5(n, s):
    if s in K.M5[n]: return True
    return False

def check_for_key(I):
    chk3 = check_for_3(I)
    if  chk3 != "g":
        for n in range (I + 1, I + 1001):
            if check_for_5(n, chk3):
                print len(K.eys) + 1, I, K.Hs[I], K.M3[I],
                print n, K.Hs[n]
                K.eys.append(I); return True
    return False

#######################################################################
# Main Routine
print ""
i = 0
for j in range (0, 1001):
    hash_stretch(j)
while len(K.eys) < 64:
    check_for_key(i)
    i += 1; hash_stretch(i + 1000)
# print 10, K.Hs[10], K.M3[10], 89, K.Hs[89], K.M5[89]
print "\n"
