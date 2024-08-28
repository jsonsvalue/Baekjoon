import sys
read = sys.stdin.readline

N = int(read().strip())
val_list = list(map(int ,read().strip().split()))
cal_list = list(map(int ,read().strip().split()))


mx = -1000000000
mn = 1000000000


def dfs(n, temp):
    global mx, mn

    if n == N-1:
        mx = max(temp, mx)
        mn = min(temp, mn)    
        return 
    
    if cal_list[0] != 0:
        cal_list[0] -= 1
        dfs(n+1, temp + val_list[n+1])
        cal_list[0] += 1

    if cal_list[1] != 0:
        cal_list[1] -= 1
        dfs(n+1, temp - val_list[n+1])
        cal_list[1] += 1

    if cal_list[2] != 0:
        cal_list[2] -= 1
        dfs(n+1, temp * val_list[n+1])
        cal_list[2] += 1

    if cal_list[3] != 0:
        cal_list[3] -= 1
        dfs(n+1, int(temp / val_list[n+1]))
        cal_list[3] += 1


dfs(0, val_list[0])
print(mx)
print(mn)    

