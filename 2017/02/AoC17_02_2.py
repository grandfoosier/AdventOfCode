fname = "AoC17_02_1.txt"
text_array = [line for line in open(fname)]
print "\nArray Opened\n"

n_array = []
for i in range(len(text_array)):
    n_array.append([])
    while True:
        j = text_array[i].find("\t")
        if j>0:
            n_array[i].append(int(text_array[i][:j]))
            text_array[i]=text_array[i][j+1:]
        else:
            j = text_array[i].find("\n")
            n_array[i].append(int(text_array[i][:j]))
            break
print "Array Loaded\n"

l = []
for i in range(len(n_array)):
    for j in range(len(n_array[i])):
        for k in range(j+1, len(n_array[i])):
            if (n_array[i][j] / n_array[i][k] ==
                n_array[i][j] * 1.0 / n_array[i][k]):
                l.append(n_array[i][j] / n_array[i][k])
            if (n_array[i][k] / n_array[i][j] ==
                n_array[i][k] * 1.0 / n_array[i][j]):
                l.append(n_array[i][k] / n_array[i][j])

print sum(l)
print "\n"
