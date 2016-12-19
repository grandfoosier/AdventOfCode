#######################################################################
#
def small_test(N):
    elves = []
    for i in range (N):
        elves.append(i + 1)
    it = 1
    while len(elves) > 1:
        m = len(elves) / 2
        out = elves.pop((elves.index(it) + m) % len(elves))
        it = elves[(elves.index(it) + 1) % len(elves)]
    return elves[0]

def which_elf(N):
    j = 0
    while 3**j < N: j += 1
    L = 3**(j - 1); M = L*2; U = L*3

    if N < M: which = N - L
    else: which = L + 2*(N - M)

    return which

#######################################################################
# Main Routine
print ""

# for i in range (2, 100):
#     print "%i:" % i, small_test(i), which_elf(i)

print "3001330:", which_elf(3001330)

print "\n"
