from hashlib import md5

def get_char():
    current = 0; psw = "________"; found = 0
    while True:
        for i in range (1000000):
            hexhash = md5("reyedfim" + str(current)).hexdigest()
            current += 1
            if hexhash[0: 5] == "00000":
                if ((int(hexhash[5], 16) in range (0, 8)) and
                            (psw[int(hexhash[5], 16)] == "_")):
                    psw = (psw[: int(hexhash[5])] + hexhash[6] +
                           psw[int(hexhash[5]) + 1: ])
                    found += 1
                    if found == 8:
                        print "\r%i" % current, psw, hexhash
                        return psw
                print "\r%i" % current, psw, hexhash
        print "\r%i" % current,

print ""
psw = get_char()
print "\n"
