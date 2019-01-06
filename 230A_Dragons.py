def A230():
    s, n = map(int, input().split(" "))
    level = 0
    for i in range(n):
        x, y = sorted(map(int, input().split(" ")))
        if s > x:
            s += y
        else:
            break
        level += 1

    if level == n:
        print('YES')
    else:
        print('NO')

if __name__=='__main__':
    A230()