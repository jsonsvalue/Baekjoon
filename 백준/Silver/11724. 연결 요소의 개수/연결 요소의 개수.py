n,m = list(map(int, input().split()))
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
count = 0

for i in range(m):
    x,y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

def dfs(vx):
    visited[vx] = True
    #해당 그래프에서의 정점에서 확인 
    for i in graph[vx]:
        # 방문한 노드가 아닌 것이 확인
        if visited[i] == False:
            dfs(i)
            
#해당 그래프에서의 각 정점에서, dfs 함수를 써서 그 순환이 마무리되면 count+1

for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        count+=1

print(count)