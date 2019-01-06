n = str(input())
s = ""
v = ['u','e','o','a','i','y']
n = n.lower()
list = list(n)
for i in n:
    if i not in v:
        s += '.'
        s += i

print(s)
