import sys
read = sys.stdin.readline

from collections import deque

n = int(read().strip())
graph = []
q = deque()

for i in range(n):
    line = list(read().rstrip())
    graph.append(line)
    

def bfs(x,y):
    q.append((x,y))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] =1
                q.append((nx,ny))

# 적색과 녹색의 경우, visited 행렬이 다르게 형성되므로 서로 다른 visited 행렬을 구성해야 한다.
# 적록색약이 아닌 경우
visited = [[0]*n for i in range(n)]
cnt1 =0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1+=1

# 적록색약이 맞는 경우
# 적색과 녹색을 똑같은 색으로 처리하고, bfs함수를 실행한다.
visited = [[0]*n for i in range(n)] 
cnt2=0
for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]='G'

for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)
                cnt2+=1

print(cnt1, cnt2)
