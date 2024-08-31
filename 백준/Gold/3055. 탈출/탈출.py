import sys
from collections import deque

read = sys.stdin.readline
row, col = map(int,read().strip().split())

# 고슴도치와 물이 이동한 위치를 저장하는 행렬
vis = [[0]*col for _ in range(row)]
q = deque()

graph = []
for i in range(row):
    row_graph = list(map(str,read().strip()))
    graph.append(row_graph)

# 비버 집 저장
for i in range(row):
    for j in range(col):
        if graph[i][j] == 'D':
            c,d = i,j

# 하나의 큐에 고슴도치 집과 물의 위치를 저장함으로써, 1초가 기준으로 bfs에서의 조건에 따라 고슴도치와 물의 위치를 저장할 수 있다.
# 고슴도치 집 저장
for i in range(row):
    for j in range(col):
        if graph[i][j] == 'S':
            x,y = i,j
            q.append((x,y))

#물의 위치 저장
for i in range(row):
    for j in range(col):
        if graph[i][j] == '*':
            q.append((i,j))


def bfs(hi, hj):
    vis[hi][hj] =1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        ci, cj = q.popleft()

        for i in range(4):
            nx = ci + dx[i]
            ny = cj + dy[i]

            if graph[ci][cj] == 'S' and 0<= nx < row and 0<= ny <col and (graph[nx][ny]=='.' or graph[nx][ny] =='D'):
                vis[nx][ny] = vis[ci][cj] + 1
                graph[nx][ny] = 'S'
                q.append((nx,ny))
            
            elif graph[ci][cj] == '*' and 0<= nx < row and 0<= ny <col and (graph[nx][ny]=='.' or graph[nx][ny] =='S'):
                graph[nx][ny] = '*'
                q.append((nx,ny))


bfs(x,y)

if vis[c][d]:
    print(vis[c][d]-1)
else:
    print('KAKTUS')
