import re

class Particles(object):
    def __init__(self):
        fname = "AoC17_20_1.txt"
        self.all = [re.split('<|>|,',line.rstrip("\n"))
                    for line in open(fname)]
        self.N = len(self.all)
        self.px = {}; self.py = {}; self.pz = {}
        self.vx = {}; self.vy = {}; self.vz = {}
        self.ax = {}; self.ay = {}; self.az = {}
        for i in range(len(self.all)):
            self.px[i] = int(self.all[i][1])
            self.py[i] = int(self.all[i][2])
            self.pz[i] = int(self.all[i][3])
            self.vx[i] = int(self.all[i][6])
            self.vy[i] = int(self.all[i][7])
            self.vz[i] = int(self.all[i][8])
            self.ax[i] = int(self.all[i][11])
            self.ay[i] = int(self.all[i][12])
            self.az[i] = int(self.all[i][13])

    def find_min_a(self):
        alist = []
        for i in range(len(self.all)):
            alist.append(abs(self.ax[i])+abs(self.ay[i])+abs(self.az[i]))
        amin = min(alist)
        pmins = [k for k,v in enumerate(alist) if v == amin]
        print pmins

    def adv_t(self):
        for p in self.px:
            self.vx[p] += self.ax[p]
            self.vy[p] += self.ay[p]
            self.vz[p] += self.az[p]
            self.px[p] += self.vx[p]
            self.py[p] += self.vy[p]
            self.pz[p] += self.vz[p]

        for p in range(self.N):
            try:
                x = self.px[p]; y = self.py[p]; z = self.pz[p]
                cols = [i for i in self.px if (
                    self.px[i] == x and self.py[i] == y and self.pz[i] == z)]
                if len(cols) > 1:
                    print "Collision at %s, %s, %s!" % (x, y, z)
                    print "Particles %s annihilate." % cols
                    for i in cols:
                        del(self.px[i]); del(self.py[i]); del(self.pz[i])
                        del(self.vx[i]); del(self.vy[i]); del(self.vz[i])
                        del(self.ax[i]); del(self.ay[i]); del(self.az[i])
                    print "%i particles remain." % len(self.px)
                    pause = raw_input("")
            except: pass
P = Particles()

print ""
while True:
    P.adv_t()
print "\n"
