def run(input):
    strng = input[0]
    i = 0
    while i < len(strng)-1:
        if (((strng[i].upper() == strng[i+1]) and
             (strng[i+1].lower() == strng[i])) or
            ((strng[i+1].upper() == strng[i]) and
             (strng[i].lower() == strng[i+1]))):
            strng = strng[:i] + strng[i+2:]
            i = max(0, i-1)
        else: i += 1
    print('units:', len(strng))

if __name__ == '__main__':
    with open('AoC18_05.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run(input)
    print('\n')
