n = 325489

def steps(n):
    i = 1
    while True:
        if n <= (2*i+1)**2: break
        else: i+=1

    sol = i + min((n + i-1)%(i*2),
                i*2 - (n + i-1)%(i*2))

    return sol

print ""
print steps(n)
