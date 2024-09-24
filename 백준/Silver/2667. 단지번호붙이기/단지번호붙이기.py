#BFS
import sys
from collections import deque
read = sys.stdin.readline

n = int(read().strip())

graph = []
result = []

for i in range(n):
    line = list(map(int, read().strip()))
    graph.append(line)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(graph, x, y):    
    graph[x][y] = 0
    count = 1

    queue = deque()
    queue.append((x,y))

    while queue:
        #Graph에 처음 추가될 때, 해당 위치를 0으로 처리해야 한다.
        x, y = queue.popleft()
        graph[x][y] = 0

        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <n and 0 <= ny < n:
                # 해당 위치가 1일 때, 주변의 집이 있는 곳의 위치를 queue에 추가한다.
                # 그럼으로써 queue에 추가된 주변의 집에서 다시 주변의 집을 탐색해서, queue가 빌 때까지 bfs 함수가 실행될 것이다.
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    count+=1
    
    return count


for i in range(n):
    for j in range(n):
        # graph에서 집이 존재한다면 bfs함수를 실행해서 해당 위치의 집 주변에 존재하는 집들의 수를 구하고,
        # 단지 내 집의 수를 result 리스트에 추가한다.
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            result.append(count)

result.sort()

print(len(result))
for cnt in result:
    print(cnt)