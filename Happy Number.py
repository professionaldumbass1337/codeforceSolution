def happyNumber():

    n = int(input())
    thelist = []

    while True:
        n = sum(map(lambda x:x*x,[int(i) for i in str(n)]))
        if n != 1:
            if n in thelist:
                print('UNHAPPY')
                break
            else:
                thelist.append(n)
        else:
            print('HAPPY')
            break

if __name__=='__main__':
    happyNumber()