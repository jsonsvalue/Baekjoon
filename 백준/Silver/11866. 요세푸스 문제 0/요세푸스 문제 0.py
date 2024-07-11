import sys

n,k = list(map(int, sys.stdin.readline().split()))
idx = 0
queue = [i for i in range(1, n+1)]
jsphs_prm = []


while queue:
    idx += k-1
    if idx >= len(queue):
        idx %= len(queue)
    jsphs_prm.append(queue.pop(idx))

print("<", ", ".join(map(str, jsphs_prm)), ">", sep = "")
    
    