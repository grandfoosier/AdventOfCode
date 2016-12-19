#######################################################################
#
def which_elf(N):
    W = 0; S = 1
    while N > 1:
        if (N % 2): W += 2 ** S
        N /= 2; S += 1
    return W + 1

#######################################################################
# Main Routine
print ""

# print which_elf(5)
# print which_elf(10)
# print which_elf(15)
# print which_elf(16)
print which_elf(3001330)

print "\n"
