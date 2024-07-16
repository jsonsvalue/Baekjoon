n= int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
ans = []

for i in range(m):
    x,y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(vx):
    visited[vx] = True
    for i in graph[vx]:
        if visited[i] == False:
            dfs(i)
            ans.append(i)
     
    return ans

print(len(dfs(1)))    
    
    