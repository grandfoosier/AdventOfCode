class Generator(object):
    def __init__(self, M, D, X):
        self.M = M; self.D = D; self.X = X
    def seed(self, N): self.N = N
    def out(self):
        self.N = (self.N * self.M) % self.D
        if self.N % self.X == 0: return ("%08x" % self.N)[-4:]
        return self.out()

d = 2147483647
A = Generator(16807, d, 4); B = Generator(48271, d, 8)
# A.seed(65); B.seed(8921)
A.seed(722); B.seed(354)

def comp_gens():
    a = A.out(); b = B.out()
    return a == b

def comp_for_i_print(i):
    c = 0; x = 0
    while True:
        print "\rGenerating pairs: %i%%" % (x * 100 / i), c,
        for j in range(i/100):
            if x == i: return c
            c += comp_gens()
            x += 1

def comp_for_i(i):
    c = 0
    for j in range(i): c += comp_gens()
    return c

print ""
c = comp_for_i_print(5000000)
print "\rGenerating pairs: 100%", c
print "\n"
