x=[]
y=[]
n=int(input())
for i in range(n):
    xi,yi=map(int,input().split())
    x.append(xi)
    y.append(yi)
a, b = 0, 0

P = sum(x)
Q = sum(y)
R = sum([x[i]*y[i] for i in range(n)])
S = sum([X**2 for X in x])

def partial_deri():

    da = (b*P-R)/S
    db = Q-a*P
    return da, db

rate = 0.0001
for j in range(10000):
    da, db = partial_deri()
    a, b = a - rate*da, b - rate*db
    print(a)
    print(b)