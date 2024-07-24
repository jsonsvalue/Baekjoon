import sys

n = int(sys.stdin.readline().strip())
seq_list = list(map(int, sys.stdin.readline().strip().split()))

sorted_seq_list = sorted(set(seq_list))
m = len(sorted_seq_list)

# For debugging purposes
# print(sorted_seq_list)

matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        curr = sorted_seq_list[i-1]
        ele_list = seq_list[j-1]
        # 현재 원소와 비교하려는 원소가 같다면, 그 이전 원소와 비교하려는 전 원소의 원소에 1을 더한다
        if curr == ele_list:
            matrix[i][j] = matrix[i-1][j-1] + 1
        # 그렇지 않고 현재의 원소가 비교하려는 원소와 같지 않다면, 같은 행의 전열과 같은 열의 전행에서 비교한 것 중에서 더 큰 것을 현재 원소로 가져온다.
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

# The length of the longest increasing subsequence will be the maximum value in the last row of the matrix

# print(matrix)

max_lis = max(matrix[m])

print(max_lis)