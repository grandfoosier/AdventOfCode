l = 1; z = 0; p = 0; n = 359; a = 0

print ""

for i in range(100):
    for j in range(500000):
        p = (p + n) % l
        l += 1
        p = (p + 1) % l

        if p == (z + 1) % l:
            a = 500000*i + j + 1
        elif p == z: z += 1
    print "\r%i%% complete" % (i+1),

print "\r%i              \n\n" % a
