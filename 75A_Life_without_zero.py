def delezero(x):
    x = x.replace("0", "")
    return x


a = input()
b = input()

if int(delezero(a)) + int(delezero(b)) == int(delezero(str(int(a)+int(b)))):
    print('YES')
else:
    print('NO')
