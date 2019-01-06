import collections

d = {}
n = int(input())
for i in range(n):
    i, d[i] = map(int, input().split())
d = collections.OrderedDict(sorted(d.items()))
print(d)