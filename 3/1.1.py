a = [10, 1, 2, 4, 5]
i = 0

for x in a:
    i += x

print(i)
i = 0
u = 0

while u != len(a):
    i += a[u]
    u += 1

print(i)