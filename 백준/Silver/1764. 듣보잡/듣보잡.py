n, m = map(int, input().split())

listen_list = []
for x in range(n):
    name = input().strip()
    listen_list.append(name)

see_list = []
for y in range(m):
    name = input().strip()
    see_list.append(name)

listen_set = set(listen_list)
see_set = set(see_list)

combine = listen_set & see_set
result = sorted(combine)

print(len(result))
for name in result:
    print(name)

