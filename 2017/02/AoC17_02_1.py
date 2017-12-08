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

sol = sum(max(l) - min(l) for l in n_array)
print sol
print "\n"
