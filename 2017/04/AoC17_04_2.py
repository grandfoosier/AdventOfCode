fname = "AoC17_04_1.txt"
lsts = [line.split() for line in open(fname)]
print "\nPassphrases Loaded\n"

srtd = [[''.join(sorted(w)) for w in l] for l in lsts]

sol = len([l for l in srtd if sorted(l) == sorted(set(l))])
print sol
print "\n"
