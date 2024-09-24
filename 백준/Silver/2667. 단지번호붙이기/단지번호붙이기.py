#DFS
import sys
from collections import deque

read = sys.stdin.readline

n = int(read().strip())

graph = []
result = []
count = 0

for i in range(n):
    line = list(map(int,read().strip()))
    graph.append(line)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#DFS를 실행하기 위한 함수를 설정한다.
def dfs(x, y):
    global count 

    if x < 0 or x >= n or y < 0 or y >= n:
        return 
    
    if graph[x][y] ==1:
        count+=1
        #방문을 했다는 표시를 하기 위해서 graph[x][y] = 0
        graph[x][y]=0
        for i in range(4):
            nx = x + dx [i]
            ny = y + dy [i]
            dfs(nx,ny)

# 여러 지점을 시작점으로 해서 DFS 함수를 실행하기 위해서는, For 문을 이용해야만 몇 개의 전단지 구역이 존재하고 각 구역마다 몇 개의 전단지가 있는지를 확인할 수 있다.
for i in range(n):
    for j in range(n):
        #그래프에 있는 위치가 전단지를 갖고 있다면, DFS함수를 실행한다.
        if graph[i][j] == 1:
            dfs(i,j)
            #해당 단지에 있는 전단지의 개수를 result에 삽입한다.
            result.append(count)
            # 새로운 단지에서 다시 전단지의 개수를 세기 위해서, count = 0 을 만든다.
            count = 0

result.sort()

print(len(result))

for cnt in result:
    print(cnt)

# print(graph)
