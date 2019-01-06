def main():
    luckynum = '47'
    n = input()
    count = 0
    yea = 0
    for c in n:
        if c in luckynum:
            count += 1
        else:
            pass

    for z in str(count):
        if z not in luckynum:
            yea += 1
            print('NO')
            break
        else:
            pass

    if yea == 0:
        print('YES')


if __name__ == '__main__':
    main()