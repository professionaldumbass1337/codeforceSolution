def A999():
    n, k = map(int, input().split())
    aList = list(map(int, input().split(' ')))
    count = 0

    for i in aList:
        if i > k:
            pass
        else:
            del aList[0]
            count += 1

    for i in reversed(aList):
        if i > k:
            break
        else:
            count += 1

    print(count)


if __name__ == '__main__':
    A999()
