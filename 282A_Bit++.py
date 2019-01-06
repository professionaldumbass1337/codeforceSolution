def A282():
    n = int(input())
    x = 0
    for i in range(n):
        i = input()
        if '++' in i:
            x += 1
        else:
            x -= 1
    print(x)

if __name__=='__main__':
    A282()