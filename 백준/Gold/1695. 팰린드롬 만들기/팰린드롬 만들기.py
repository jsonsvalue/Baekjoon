import sys
read = sys.stdin.readline

n = int(read().strip())
num_list = list(map(int, read().strip().split()))

dp = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        #수열의 끝 숫자와 수열의 앞 숫자가 대응하는지 확인한다
        if num_list[-i] == num_list[j-1]:
            # 수열의 끝에서 i-1개의 숫자에서 수열의 처음 j-1개의 숫자에서 공통되는 숫자 +1 
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 수열의 끝에서 i-1개 수열의 앞에서 j개, 수열의 끝에서 i개 수열의 앞에서 j-1개까지 공통되는 숫자의 개수 중 큰 것을 저장한다
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 전체 숫자의 개수에서 공통되는 부분을 찾으면, 내가 추가해야되는 숫자의 최소 개수를 알 수 있다
print(n - dp[-1][-1])
