import sys

read = sys.stdin.readline

matrix = []

n = int(read())

for i in range(n):
    line = list(map(int, read().split()))
    matrix.append(line)

dp_mtrx = [[0] * n for _ in range(n)]
dp_mtrx[0][0] = 1

for i in range(n):
    for j in range(n):
        #마지막 지점까지 도달했을 때, 혹은 가는 경로 자체가 없는 지점은 확인하지 않는 것
        if matrix[i][j] == 0 or dp_mtrx[i][j]==0:
            continue

        jump_distance = matrix[i][j]
        n_down = j + jump_distance
        n_right = i + jump_distance

        if n_down < n:
            dp_mtrx[i][n_down] += dp_mtrx[i][j]

        if n_right < n:
            dp_mtrx[n_right][j] += dp_mtrx[i][j] 



print(dp_mtrx[n-1][n-1])        

            
        
