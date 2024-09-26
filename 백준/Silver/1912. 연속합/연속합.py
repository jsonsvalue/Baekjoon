import sys
read = sys.stdin.readline

n = int(read().strip())

num_list = list(map(int,read().split()))

for i in range(1,n):
    num_list[i] = max(num_list[i], num_list[i-1]+num_list[i])

print(max(num_list))

