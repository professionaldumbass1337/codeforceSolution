n = list(input().split("+"))
n.sort()
m = ""

for i in n:
    m += str(i) + "+"
m = m[:-1]

print(m)