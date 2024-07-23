import sys

n, k = map(int ,sys.stdin.readline().split())

coin_list = []

for i in range(n):
    coin = int(sys.stdin.readline())
    coin_list.append(coin)

coin_list.sort(reverse = True)

count = 0

while k!=0:
    for i in range(len(coin_list)):
        count+= k // coin_list[i]
        k -= k//coin_list[i] * coin_list[i]

print(count)

    