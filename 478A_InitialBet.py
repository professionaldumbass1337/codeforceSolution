a = list(map(int, input().split()))
print('-1' if sum(a) % 5 != 0 or sum(a) == 0 else int(sum(a)/5))