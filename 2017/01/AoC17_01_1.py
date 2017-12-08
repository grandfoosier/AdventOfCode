fname = "AoC17_01_1.txt"
text = [line.rstrip('\n') for line in open(fname)][0]
print "\nInteger Stream Loaded\n"

n = len(text)
sol = sum(int(c) for i,c in enumerate(text)
    if text[i] == text[(i+1)%n])
print sol
print "\n"
