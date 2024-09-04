import sys
from collections import deque

read = sys.stdin.readline

m, n, h = map(int,read().strip().split())
graph = [[list(map(int,read().strip().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0<= nz < h:
                if graph[nz][nx][ny] ==0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    #print(graph[nz][nx][ny])
                    queue.append((nz, nx, ny))

# 익어 있는 토마토를 탐색을 통해서 찾고, 큐에 삽입한다.
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

# 익어 있는 토마토의 큐에서 bfs를 통해, 모든 방향의 토마토를 탐색하여 익게 만든다.  
bfs()

# 익은 토마토가 안 익은 토마토에 영향을 줘서, 전체 상자의 토마토가 익는 데 걸리는 일수를 구한다. 
complete = True
max_days = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] ==0:
                complete = False
            max_days = max(max_days, graph[i][j][k])

if complete:
    print(max_days-1)
else:
    print(-1)









