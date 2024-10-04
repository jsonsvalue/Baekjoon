import sys
read = sys.stdin.readline

def w(a,b,c):
    if a <=0 or b<=0 or c<=0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    
    # dp[a][b][c]의 값이 존재한다면 w(a,b,c) = dp[a][b][c]를 저장해야, w(a,b,c) 재귀함수 계산 속도를 높일 수 있다. 
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        # print("조건")
        # print(dp[a][b][c])
        return dp[a][b][c]
    
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1,c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    # print("미충족")
    # print(dp[a][b][c])
    return dp[a][b][c]


#0~20 까지만 연산이 되기 때문에, 해당 범위로 설정한다.
dp = [[[0]*21 for _ in range(21)]for _ in range(21)]


while True:
    a, b, c = list(map(int,read().strip().split()))
    
    if a ==-1 and b ==-1 and c ==-1:
        break
    
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
