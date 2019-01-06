def A25():
    n = int(input())
    even = odd = lasteven = lastodd = 0
    x = list(map(int, input().split()))
    for i in x:
        if i % 2 == 0:
            even += 1
            lasteven = x.index(i) + 1
        else:
            odd += 1
            lastodd = x.index(i) + 1

    if even > odd:
        print(lastodd)
    else:
        print(lasteven)


if __name__ == '__main__':
    A25()
