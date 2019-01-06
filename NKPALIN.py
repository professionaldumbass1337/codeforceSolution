def main():
    n = (str(input()))
    c = n[::-1]
    z = set(n)
    t = set(c)

    print(1)
    print(z & t)


if __name__=='__main__':
    main()