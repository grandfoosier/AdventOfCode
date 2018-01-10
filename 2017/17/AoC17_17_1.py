class Bufr(object):
    def __init__(self, n):
        self.ufr = [0]
        self.p = 0
        self.n = n
# B = Bufr(3)
B = Bufr(359)

def adv(i):
    B.p = (B.p + B.n) % len(B.ufr)
    B.ufr = B.ufr[:B.p+1] + [i] + B.ufr[B.p+1:]
    B.p = (B.p + 1) % len(B.ufr)

print ""
for i in range (2017):
    adv(i+1)
print B.ufr[(B.p + 1) % len(B.ufr)]
print "\n"
