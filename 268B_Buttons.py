def B268():
    n = int(input())
    i = 1
    k = 0
    while i !=n :
        k += i*(n-i)
        i += 1

    print(n+k)


if __name__=='__main__':
    B268()