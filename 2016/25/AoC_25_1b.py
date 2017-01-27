A = 0
B = 362 * 7

while A < B:
    A = 2*A + 1
    if A > B: break
    A *= 2

print A - B
