n, m, a = map(int, input().split())

width = int(n / a)
length = int(m / a)
if n % a != 0:
    width += 1
if m % a != 0:
    length += 1
print(str(width * length))