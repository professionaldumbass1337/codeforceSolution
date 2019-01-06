height, width = map(int, input().split())
aList = []
Color = 'CMY'
for i in range(height):
    aList.append(input().split())
for j in aList:
    for k in j:
        if k in Color:
            print("#Color")
            exit()
        else:
            pass

print("#Black&White")