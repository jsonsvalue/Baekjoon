import sys

n, l = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(l+1)] for _ in range(n+1)]

knap_list = []
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    knap_list.append((w,v))

for i in range(1,n+1):
    w, v = knap_list[i-1]
    for j in range(1, l+1):
        if w <= j:
            matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-w] + v)
        else:
            matrix[i][j] = matrix[i-1][j]

print(matrix[n][l])

    