import sys
inp_str1  = sys.stdin.readline().strip()
inp_str2 = sys.stdin.readline().strip()

n = len(inp_str1) 
m = len(inp_str2)

matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

str1 = list(inp_str1)
str2 = list(inp_str2)
# print(str1)
# print(str2)



for i in range(1, n+1):
    for j in range(1, m+1):       
        if str1[i-1] == str2[j-1]:
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
            matrix [i][j] = max(matrix[i][j-1], matrix[i-1][j])

# print(matrix)

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if i==0:
#             matrix[i][j] = 0
#         else:
#             if j==0:
#                 matrix[i][j] =0
            
#             else:
#                 if str1[i] == str2[j]:
#                     matrix[i][j] +=1
#                 else:
#                     matrix [i][j] = max(matrix[i][j-1], matrix[i-1][j])

print(matrix[n][m])





