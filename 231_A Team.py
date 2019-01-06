def A231():
    n = int(input())
    count = 0
    for aList in range(n):
        aList = list(map(int, input().split()))
        if sum(aList) < 2:
            pass
        else:
            count += 1

    print(count)

if __name__=='__main__':
    A231()