import re

class Particles(object):
    def __init__(self):
        fname = "AoC17_20_1.txt"
        self.all = [re.split('<|>|,',line.rstrip("\n"))
                    for line in open(fname)]
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
P = Particles()

print ""
P.find_min_a()
print "\n"
