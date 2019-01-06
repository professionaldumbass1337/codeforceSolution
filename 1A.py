class waterMelon:
    def solve(self, x):
        if (x<=2 or  x>=109):
            return "NO"
        elif ((x-2)%2==0):
            return "YES"
        else :
            return "NO"

if __name__=='__main__':
    x = int(input())
    z = waterMelon()
    print(z.solve(x))
