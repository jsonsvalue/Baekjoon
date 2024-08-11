import sys
read = sys.stdin.readline

def fact(n):
    if n==0:
        return 1    
    return n * fact(n-1)

n = int(read().strip())
print(fact(n))
