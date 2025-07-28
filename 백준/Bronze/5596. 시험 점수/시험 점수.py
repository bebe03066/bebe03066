a = list(map(int, input().split()))

b = list(map(int, input().split()))

a_total = sum(a)

b_total = sum(b)

if a_total >= b_total: 
    print(a_total)
else:
        print(b_total)