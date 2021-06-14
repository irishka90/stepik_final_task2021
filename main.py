n = int(input())
a = []
# a = [[0 for j in range(n)] for i in range(n)]
q = 1
for i in range(n):
    for j in range(n):
        a.append(q)
        q += 1
        print(a)
z = [[0 for j in range(n)] for i in range(n)]
print(z)
for i in range(n):
    for j in range(n):
        z[0][0] = a[0]



print(z)

# for i in range(n):
# for j in range(n):
# print(a[i][j], end='')
#  print()
