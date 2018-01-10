class Art(object):
    def __init__(self):
        fname = "AoC17_21_1.txt"
        self.rules = [line.rstrip("\n").split() for line in open(fname)]
        self.lkup = [i[0] for i in self.rules]
        self.grid = ['.#.','..#','###']

    def _twfh(self, s):
        return (s[1] + s[0] + '/' + # 01 -> 10
                s[4] + s[3])        # 34 -> 43
    def _twfv(self, s):
        return (s[3] + s[4] + '/' + # 01 -> 34
                s[0] + s[1])        # 34 -> 01
    def _twr1(self, s):
        return (s[3] + s[0] + '/' + # 01 -> 30
                s[4] + s[1])        # 34 -> 41
    def _twr2(self, s):
        return (s[4] + s[3] + '/' + # 01 -> 43
                s[1] + s[0])        # 34 -> 10
    def _twr3(self, s):
        return (s[1] + s[4] + '/' + # 01 -> 14
                s[0] + s[3])        # 34 -> 03
    def _twf1(self, s):
        return (s[4] + s[1] + '/' + # 01 -> 41
                s[3] + s[0])        # 34 -> 30
    def _twf3(self, s):
        return (s[0] + s[3] + '/' + # 01 -> 03
                s[1] + s[4])        # 34 -> 14

    def _thfh(self, s):
        return (s[2] + s[1] + s[0] + '/' +  # 012    210
                s[6] + s[5] + s[4] + '/' +  # 456 -> 654
                s[10] + s[9] + s[8])        # 89A    A98
    def _thfv(self, s):
        return (s[8] + s[9] + s[10] + '/' + # 012    89A
                s[4] + s[5] + s[6] + '/' +  # 456 -> 456
                s[0] + s[1] + s[2])         # 89A    012
    def _thr1(self, s):
        return (s[8] + s[4] + s[0] + '/' +  # 012    840
                s[9] + s[5] + s[1] + '/' +  # 456 -> 951
                s[10] + s[6] + s[2])        # 89A    A62
    def _thr2(self, s):
        return (s[10] + s[9] + s[8] + '/' + # 012    A98
                s[6] + s[5] + s[4] + '/' +  # 456 -> 654
                s[2] + s[1] + s[0])         # 89A    210
    def _thr3(self, s):
        return (s[2] + s[6] + s[10] + '/' + # 012    26A
                s[1] + s[5] + s[9] + '/' +  # 456 -> 159
                s[0] + s[4] + s[8])         # 89A    048
    def _thf1(self, s):
        return (s[10] + s[6] + s[2] + '/' + # 012    A62
                s[9] + s[5] + s[1] + '/' +  # 456 -> 951
                s[8] + s[4] + s[0])         # 89A    840
    def _thf3(self, s):
        return (s[0] + s[4] + s[8] + '/' +  # 012    048
                s[1] + s[5] + s[9] + '/' +  # 456 -> 159
                s[2] + s[6] + s[10])        # 89A    26A

    def _tw2th(self):
        fmd = []
        for i in range(len(self.grid)/2):
            fmd.append([])
            for j in range(len(self.grid)/2):
                fmd[i].append(self.grid[2*i][2*j:2*j+2] + '/' +
                              self.grid[2*i+1][2*j:2*j+2])

        new = []
        for i in range(len(fmd)):
            new.append([])
            for j in fmd[i]:
                if j in self.lkup:
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._twfh(j) in self.lkup:
                    j = self._twfh(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._twfv(j) in self.lkup:
                    j = self._twfv(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._twr1(j) in self.lkup:
                    j = self._twr1(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._twr2(j) in self.lkup:
                    j = self._twr2(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._twr3(j) in self.lkup:
                    j = self._twr3(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._twf1(j) in self.lkup:
                    j = self._twf1(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._twf3(j) in self.lkup:
                    j = self._twf3(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                else:
                    pause = raw_input("OOPS")

        self.grid = []
        for i in range(len(new)):
            self.grid.extend(['','',''])
            for j in range(len(new)):
                self.grid[3*i+0] += new[i][j][0:3]
                self.grid[3*i+1] += new[i][j][4:7]
                self.grid[3*i+2] += new[i][j][8:11]

    def _th2fo(self):
        fmd = []
        for i in range(len(self.grid)/3):
            fmd.append([])
            for j in range(len(self.grid)/3):
                fmd[i].append(self.grid[3*i][3*j:3*j+3] + '/' +
                              self.grid[3*i+1][3*j:3*j+3] + '/' +
                              self.grid[3*i+2][3*j:3*j+3])

        new = []
        for i in range(len(fmd)):
            new.append([])
            for j in fmd[i]:
                if j in self.lkup:
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._thfh(j) in self.lkup:
                    j = self._thfh(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._thfv(j) in self.lkup:
                    j = self._thfv(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._thr1(j) in self.lkup:
                    j = self._thr1(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._thr2(j) in self.lkup:
                    j = self._thr2(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._thr3(j) in self.lkup:
                    j = self._thr3(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._thf1(j) in self.lkup:
                    j = self._thf1(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                elif self._thf3(j) in self.lkup:
                    j = self._thf3(j)
                    x = self.lkup.index(j)
                    new[i].append(self.rules[x][2])
                else:
                    pause = raw_input("OOPS")

        self.grid = []
        for i in range(len(new)):
            self.grid.extend(['','','',''])
            for j in range(len(new)):
                self.grid[4*i+0] += new[i][j][0:4]
                self.grid[4*i+1] += new[i][j][5:9]
                self.grid[4*i+2] += new[i][j][10:14]
                self.grid[4*i+3] += new[i][j][15:19]

    def increment(self, n):
        for i in range(n):
            print i+1
            if len(self.grid) % 2 == 0: self._tw2th()
            else: self._th2fo()

    def count_on(self):
        c = 0
        for i in self.grid: c += i.count('#')
        return c
A = Art()

print ""
A.increment(18)
print ""
print A.count_on()
print "\n"
