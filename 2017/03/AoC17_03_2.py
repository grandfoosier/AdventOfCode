n = 325489

nmap = {(0,0):1}
print nmap
x,y,r = 1,0,1

def find_s(x, y):
    s = 0

    try: s += nmap[(x-1,y-1)]
    except: s += 0
    try: s += nmap[(x  ,y-1)]
    except: s += 0
    try: s += nmap[(x+1,y-1)]
    except: s += 0
    try: s += nmap[(x+1,y  )]
    except: s += 0
    try: s += nmap[(x+1,y+1)]
    except: s += 0
    try: s += nmap[(x  ,y+1)]
    except: s += 0
    try: s += nmap[(x-1,y+1)]
    except: s += 0
    try: s += nmap[(x-1,y  )]
    except: s+= 0

    return s

while True:
    for a in range(r*2 -1):
        nmap[(x,y)] = find_s(x, y)
        print x, y, nmap[(x,y)]
        if nmap[(x,y)] > n: pause = raw_input("")
        y -= 1
    for a in range(r*2):
        nmap[(x,y)] = find_s(x, y)
        print x, y, nmap[(x,y)]
        if nmap[(x,y)] > n: pause = raw_input("")
        x -= 1
    for a in range(r*2):
        nmap[(x,y)] = find_s(x, y)
        print x, y, nmap[(x,y)]
        if nmap[(x,y)] > n: pause = raw_input("")
        y += 1
    for a in range(r*2 +1):
        nmap[(x,y)] = find_s(x, y)
        print x, y, nmap[(x,y)]
        if nmap[(x,y)] > n: pause = raw_input("")
        x += 1
    r += 1
