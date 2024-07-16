import sys
from collections import deque

n, m, st = list(map(int, input().split()))

#기본 그래프 형성 및 연결 관계 기록
graph = [[False] * (n+1) for i in range(n+1)]
for i in range(m):
    x, y= list(map(int, input().split()))
    graph[x][y]=1
    graph[y][x]=1

#각 노드별 방문 기록 
vst_dfs = [False] *(n+1)
vst_bfs = [False] *(n+1)

# dfs함수 만들기
# 방문 안한 노드 + 해당 노드와 연결 됐을 경우, 연결된 노드 따라서 dfs재귀
# 그러니까 한번 방문한 노드를 끝까지 방문하는 것을 의미 
def dfs(st):
    vst_dfs[st] = True
    print(st, end = " ")
    for i in range(1, n+1):
        if not vst_dfs[i] and graph[st][i]==1:
            dfs(i)

# bfs 함수 만들기 
# 해당 노드와 연결된 노드를 큐에 추가 
# 해당 노드가 방문이 됐을 때는 .popleft()를 해서 큐에서 삭제 후 프린트
# 그러니까 첫 노드에서 같은 너비에 있는 노드를 순서대로 출력한다는 것을 의미

def bfs(st):
    queue = deque([st])
    
    vst_bfs[st] = True
    while queue:
        st = queue.popleft()
        print(st, end = " ")
        for i in range(1, n+1):
            if not vst_bfs[i] and graph[st][i] ==1:
                queue.append(i)
                vst_bfs[i]= True

                
dfs(st)
print()
bfs(st)