#2nd Try
import sys
import heapq

read = sys.stdin.readline
n = int(read().strip())
num_input = list(map(int,read().strip().split()))

# Stack to store the idx of the NGE
# Storing largest index from i th number in the num_input, and comparing it with num_input
stack = []
result = [-1] * n

for i in range(n):
    #Updating the stack with a bigger number on the right, everytime it finds one 
    while stack and num_input[stack[-1]] < num_input[i]:
        idx = stack.pop()
        result[idx] = num_input[i]
    stack.append(i)

for res in result: 
    print(res)