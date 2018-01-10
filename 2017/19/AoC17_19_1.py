class Packet(object):
    def __init__(self):
        fname = "AoC17_19_1.txt"
        self.paths = [line.rstrip("\n") for line in open(fname)]
        self.dir = 'D'
        self.pos = (0, self.paths[0].find('|'))
        self.markers = ''

    def _turn(self):
        (y, x) = self.pos
        try:
            if self.dir != 'D' and self.paths[y-1][x] != ' ': return 'U'
        except: pass
        try:
            if self.dir != 'L' and self.paths[y][x+1] != ' ': return 'R'
        except: pass
        try:
            if self.dir != 'U' and self.paths[y+1][x] != ' ': return 'D'
        except: pass
        try:
            if self.dir != 'R' and self.paths[y][x-1] != ' ': return 'L'
        except: pass
        return 'X'

    def _check(self):
        (y, x) = self.pos
        try:
            if self.dir == 'U' and self.paths[y-1][x] == ' ':
                return self._turn()
        except: return self._turn()
        try:
            if self.dir == 'R' and self.paths[y][x+1] == ' ':
                return self._turn()
        except: return self._turn()
        try:
            if self.dir == 'D' and self.paths[y+1][x] == ' ':
                return self._turn()
        except: return self._turn()
        try:
            if self.dir == 'L' and self.paths[y][x-1] == ' ':
                return self._turn()
        except: return self._turn()
        return self.dir

    def _move(self):
        (y, x) = self.pos
        if   self.dir == 'U': self.pos = (y-1, x)
        elif self.dir == 'R': self.pos = (y, x+1)
        elif self.dir == 'D': self.pos = (y+1, x)
        elif self.dir == 'L': self.pos = (y, x-1)
        if self.paths[y][x] not in ['|','-','+']:
            self.markers += self.paths[y][x]

    def follow_path(self):
        while self.dir != 'X':
            self.dir = self._check()
            self._move()
        return self.markers
P = Packet()

print ""
print P.follow_path()
print "\n"
