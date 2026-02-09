
A,B = map(int, input().split())

C = A * B

D = list(map(int, input().split()))

E = [D - C for D in D]

print(*(E))