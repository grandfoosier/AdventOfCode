from hashlib import md5

def get_char():
    current = 0; psw = ""
    while True:
        for i in range (1000000):
            hexhash = md5("reyedfim" + str(current)).hexdigest()
            current += 1
            if hexhash[0: 5] == "00000":
                psw += hexhash[5]; print "\r%i" % current, psw, hexhash
                if len(psw) == 8: return psw
        print "\r%i" % current,

print ""
psw = get_char()
print "\n"
