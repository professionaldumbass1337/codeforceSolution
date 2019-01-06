def q3(x):
    if x == 'white':
        x = 'black'
    else:
        pass

def main():
    n, q = map(int, input().split())
    count01 = 2
    aDict = {1: [0, 'white']}
    p = map(int, input().split())

    for i in p:
        aDict[count01] = [i, 'white']
        count01 += 1

    for z in range(q):
        z = list(map(int, input().split()))
        print(aDict[z[1]][1])

        # if z[0] == 1:
        #     q3(aDict[z[1]][2])
        #     else;
        #
        # elif z[0] == 2:
        #
        # else:



if __name__ == '__main__':
    main()