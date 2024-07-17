from collections import deque

n,m,k,x = list(map(int, input().split()))

graph = [[] for i in range(n+1)]

visited = [-1] * (n+1)

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)

def bfs(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        vx = queue.popleft()
        for adj in graph[vx]:
            if visited[adj] == -1:
                visited[adj] = visited[vx] + 1
                queue.append(adj)
    
    return visited

bfs(x)

result = []
for i in range(1,n+1):
    if visited[i] == k:
        result.append(i)        
result.sort()

if result:
    for city in result:
        print(city)
else:
    print(-1)