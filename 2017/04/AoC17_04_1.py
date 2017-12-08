fname = "AoC17_04_1.txt"
lsts = [line.split() for line in open(fname)]
print "\nPassphrases Loaded\n"

sol = len([l for l in lsts if sorted(l) == sorted(list(set(l)))])
print sol
print "\n"
