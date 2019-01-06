n = int(input())
alist = []
m = 0
while m < n:
    alist.append(list(map(int, input().split())))
    m += 1
print(alist)
if sum(list(map(sum, zip(alist)))) == 0:
    print("YES")
else:
    print("NO")