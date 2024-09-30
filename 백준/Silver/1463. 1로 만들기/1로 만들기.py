import sys
read = sys.stdin.readline

x = int(read().strip())

dp = [0]* ((10**6) + 1)

# def count_cal(x):
#     count =0
#     while x !=1:
#         if x % 3 == 0:
#             x = x //3
#         elif x % 2 ==0:
#             x = x//2
#         else:
#             x-=1
        
#         count+=1

#     return count

def count_cal(x):
    for i in range(2,x+1):
        dp[i] = dp[i-1]+1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)

        if i % 3 ==0:
            dp[i] = min(dp[i], dp[i//3]+1)
        
    return dp[x]

print(count_cal(x))
