import sys
read = sys.stdin.readline

n = int(read().strip())
box_list = list(map(int,read().strip().split()))

dp = [1] * n

# for i in range(1,n):
#     if box_list[i-1] < box_list[i]:
#         dp[i] = dp[i-1] + 1
#     dp[i]= max(dp[i-1], dp[i])

# for i in range(n):
#     for j in range(n-1, -1, -1):
#         if box_list[i] < box_list[j]:
#             dp[j] = dp[i] + 1 
#             break
#     dp[j] = max(dp[j-1], dp[j])

for i in range(n):
    for j in range(i):
        if box_list[j] < box_list[i]:
            dp[i] = max(dp[j] + 1, dp[i])

# print(dp)
print(max(dp))
