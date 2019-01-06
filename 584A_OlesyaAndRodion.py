def A584():
    n, t = map(int, input().split())
    a = 10**(n-1)
    if n == 1 and t == 10:
        print(-1)
    else:
        while a % t != 0:
            a += 1

    print(a)

if __name__ == "__main__":
    A584()