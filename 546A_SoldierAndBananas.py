def A546():
    k, n, w = list(map(int, input().split(" ")))
    cost = k * w * (w + 1) * 0.5
    if cost > n :
        print(int(cost - n))
    else:
        print(0)

if __name__=='__main__':
    A546()
