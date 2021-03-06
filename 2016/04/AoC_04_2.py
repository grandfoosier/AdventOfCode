fname = "AoC_04_1.txt"
rooms = [line.rstrip('\n') for line in open(fname)]
print "\nRoom List Loaded\n"

class You(object):
    def __init__(self):
        self.rd = {}
        self.abc = ["a", "b", "c", "d", "e",
                    "f", "g", "h", "i", "j",
                    "k", "l", "m", "n", "o", "p",
                    "q", "r", "s", "t", "u",
                    "v", "w", "x", "y", "z"]
Me = You()

def check_room(code):
    allabc = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
              "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
              "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
              "q": 0, "r": 0, "s": 0, "t": 0, "u": 0,
              "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    bracket = code.find("[")
    ID = int(code[bracket - 3: bracket])
    checksum = code[bracket + 1: bracket + 6]

    for x in code[: bracket - 4]:
        if x in Me.abc: allabc[x] += 1

    most_common = ""
    while len(most_common) < 5:
        n = max(allabc.values())

        temp = []
        for a in allabc:
            if allabc[a] == n:
                temp.append(a)
                allabc[a] = 0
        stemp = sorted(temp)

        for i in range (min(5 - len(most_common), len(stemp))):
            most_common += stemp[i]

    decrypted = ""
    if most_common == checksum:
        for x in code[: bracket - 4]:
            if x == "-": decrypted += " "
            else: decrypted += Me.abc[(Me.abc.index(x) + ID) % 26]
        Me.rd[decrypted] = ID

# check_room("qzmt-zixmtkozy-ivhz-343[zimth]")

for room in rooms: check_room(room)
for ID in sorted(Me.rd): print Me.rd[ID], ID

print "\n"
