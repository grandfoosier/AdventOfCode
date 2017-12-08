fname = "AoC17_05_1.txt"
steps = [int(line.rstrip("\n")) for line in open(fname)]
print "\nSteps Loaded\n"

for i in range(10): print steps[i]

i = 0; n = 0

while True:
    try:
        j = i + steps[i]
        steps[i] += 1
        i = j
        n += 1
    except: break

print n
print "\n"
