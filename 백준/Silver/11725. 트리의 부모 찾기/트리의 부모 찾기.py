import sys
sys.setrecursionlimit(10**8)

n = int(input())

graph = [[] for i in range(n+1)]
visited = [-1] * (n+1)

for i in range(n-1):
    a,b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def dfs(vx):
    #해당 노드에서 연결되는 다른 노드 중에서 확인하는 작업
    for i in graph[vx]:
        # 해당 노드와 연결된 다른 노드 중 방문한 적이 없는 노드라면, 해당 노드를 부모 노드로 저장
        if visited[i] == -1:
            visited[i] = vx
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(visited[i])

