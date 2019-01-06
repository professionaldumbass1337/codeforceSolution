def B158():
    n = int(input())
    s = map(int, input().split())
    a = b = c = d = 0
    for i in s:
        if i == 1:
            a += 1
        elif i == 2:
            b += 1
            if b % 2 == 0:
                b = b/2
            else:
                b = b/2+1
        elif i == 3:
            c += 1
        else:
            d += 1
    if b+c >= a:
        print(b+c+d)
    else:
        print(a+c)

if __name__ == '__main__':
    B158()
