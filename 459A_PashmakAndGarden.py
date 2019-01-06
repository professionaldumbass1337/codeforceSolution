x1, y1, x2, y2 = map(int, input().split())

if x1 == x2 or y1 == y2:
    x3 = x4 = x1 + abs(y2-y1)
    y3 = y2
    y4 = y2
else:
    if x1 != y1 or x2 != y2:
        print(-1)
        exit()
    else:
        x3 = x1
        y3 = y2
        x4 = x2
        y4 = y1

print(str(x1)+' '+str(y2)+' '+str(x2)+' '+str(y1))