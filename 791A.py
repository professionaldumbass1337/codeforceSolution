def main():
    n, t = map(int, input().split())
    count = 0
    while n <= t:
        n *= 3
        t *= 2
        count += 1

    print(count)


if __name__=='__main__':
    main()