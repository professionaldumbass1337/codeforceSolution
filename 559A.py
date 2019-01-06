def main():
    d1, d2, d3 = map(int, input().split())
    if d3 < min(min(d1, d2), d3):
        print(2*(min(d1, d2)+d3))
    else:
        print(d1+d2+min(d1+d2,d3))

if __name__=='__main__':
    main()