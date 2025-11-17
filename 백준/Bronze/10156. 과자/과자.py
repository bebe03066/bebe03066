a,b,c = map(int, input().split())
d = a*b - c
if d<0:
    d = 0
print(d)