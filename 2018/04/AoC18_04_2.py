import re

def run():
    GDict = {}
    guardID = 0
    for line in sorted(input):
        inp = re.split(' ', line)
        if inp[2] == 'Guard':
            id = int(inp[3][1:])
            if id not in GDict:
                GDict[id] = [0] * 60
        if inp[2] == 'falls':
            start = int(inp[1][3:5])
        if inp[2] == 'wakes':
            end = int(inp[1][3:5])
            for i in range(start, end):
                GDict[id][i] += 1
    ID = max(GDict, key= lambda k: max(GDict[k]))
    print('Most Consistently Sleepy Guard:', ID)
    Min = GDict[ID].index(max(GDict[ID]))
    print('Sleepiest Minute:', Min)
    print(ID * Min)


if __name__ == '__main__':
    with open('AoC18_04.txt') as file:
        input = [line.rstrip('\n') for line in file]
    print('Input Loaded\n')
    run()
    print('\n')
