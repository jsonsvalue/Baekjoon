import sys

read = sys.stdin.readline

prth = list(read().strip())

stack1 = []
stack2 = []
is_valid = True
result = 0
temp = 1

for i in range(len(prth)):
    if prth[i] == '(':
        stack1.append('(')
        temp*= 2
    
    elif prth[i] == '[':
        stack2.append('[')
        temp*= 3

    elif prth[i] == ')':
        if stack1 and stack1[-1] == '(':
            stack1.pop()
            if prth[i-1] == '(':
                result += temp
            temp //= 2
        
        else:
            is_valid = False
            break

    elif prth[i] == ']':
        if stack2 and stack2[-1] == '[':
            stack2.pop()
            if prth[i-1] == '[':
                result +=temp
            temp//=3

        else:
            is_valid = False
            break

if stack1 or stack2:
    is_valid = False

if is_valid:
    print(result)
else:
    print(0)

