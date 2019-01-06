aList = []
black = {'q':9,'r':5,'b':3,'n':3,'p':1}
white = {'Q':9,'R':5,'B':3,'N':3,'P':1}
White = Black = 0
for i in range(8):
    aList.append(input())
for j in aList:
    for k in j:
        if k in white:
            White += white[k]
        elif k in black:
            Black += black[k]

print('White' if White>Black else ('Black' if Black>White else 'Draw'))