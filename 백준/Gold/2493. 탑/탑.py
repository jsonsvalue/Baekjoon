import sys

read = sys.stdin.readline

n = int(read().strip())
bld_list = list(map(int,read().strip().split()))

stack = []
result = []
for i in range(n):
    while stack and stack[-1][0] < bld_list[i]:
        stack.pop()

    if stack:
        # print(stack[-1][1]+1)
        result.append(stack[-1][1]+1)
    
    else:
        # print(0)
        result.append(0)

    stack.append([bld_list[i], i])

for idx in result:
    print(idx, end = ' ')