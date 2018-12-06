def run(input):
    charDict = {}
    for c in 'abcdefghijklmnopqrstuvwxyz':
        strng = input[0].replace(c.upper(),'')
        strng = strng.replace(c,'')
        i = 0
        while i < len(strng)-1:
            if (((strng[i].upper() == strng[i+1]) and
                 (strng[i+1].lower() == strng[i])) or
                ((strng[i].lower() == strng[i+1]) and
                 (strng[i+1].upper() == strng[i]))):
                strng = strng[:i] + strng[i+2:]
                i = max(0, i-1)
            else: i += 1
        print(c +':', len(strng))
        charDict[c] = len(strng)
    c = min(charDict, key = lambda k: charDict[k])
    print('\nmin:', c, '-', charDict[c])

if __name__ == '__main__':
    with open('AoC18_05_1.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(input)
    print('\n')
