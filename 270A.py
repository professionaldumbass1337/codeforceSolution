def main():
    n = int(input())
    for i in range(n):
        i = int(input())
        if i >= 60 and i < 180:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()