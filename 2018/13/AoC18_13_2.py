class Cart(object):
    def __init__(self, mapp, r, c):
        self.r = r; self.c = c
        self.turn = 'L'; self.dir = mapp[r][c]
        self.went = False; self.crashed = False

    def go(self, inpt, mapp):
        if self.went: return mapp

        r = self.r; c = self.c
        mapp[r] = mapp[r][:c] + inpt[r][c] + mapp[r][c+1:]
        (r, c) = [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]['><v^'.index(self.dir)]
        self.r = r; self.c = c

        if   mapp[r][c] == '\\': self.dir = 'v^><'['><v^'.index(self.dir)]
        elif mapp[r][c] ==  '/': self.dir = '^v<>'['><v^'.index(self.dir)]
        elif mapp[r][c] ==  '+':
            self.dir = '>v<^'[('>v<^'.index(self.dir) +
                               'SRBL'.index(self.turn)) % 4]
            self.turn = 'LSR'[('LSR'.index(self.turn)+1) % 3]
        elif mapp[r][c] in '>v<^': self.crashed = True
        mapp[r] = mapp[r][:c] + self.dir + mapp[r][c+1:]
        self.went = True; return mapp

    def cleanup(self, inpt, mapp):
        r = self.r; c = self.c
        mapp[r] = mapp[r][:c] + inpt[r][c] + mapp[r][c+1:]
        return mapp

def findcart(carts, r, c):
    for cart in carts:
        if cart.r == r and cart.c == c: return cart

def run(inpt):
    mapp = [inpt[r] for r in range(len(inpt))]; carts = []
    for r in range(len(mapp)):
        for c in range(len(mapp[r])):
            if mapp[r][c] in '>v<^':
                inpt[r] = (inpt[r][:c] + '-|-|'['>v<^'.index(mapp[r][c])] +
                           inpt[r][c+1:])
                carts += [Cart(mapp, r, c)]

    while True:
        for r in range(len(mapp)):
            for c in range(len(mapp[r])):
                if mapp[r][c] in '>v<^':
                    cart = findcart(carts, r, c)
                    mapp = cart.go(inpt, mapp)
                    if cart.crashed == True:
                        mapp = cart.cleanup(inpt, mapp)
                        carts = list(filter(lambda X:
                                     X.r != cart.r or X.c != cart.c, carts))
        for cart in carts: cart.went = False
        if len(carts) == 1:
            print(carts[0].c, carts[0].r); return

if __name__ == '__main__':
    with open('AoC18_13.txt') as file:
        inpt = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(inpt)
    print('\n')
