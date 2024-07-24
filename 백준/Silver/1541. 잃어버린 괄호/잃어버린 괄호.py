import sys

cal_str = sys.stdin.readline().strip()

# cal_str = "10+15-30+40-21+50"

minus_str = cal_str.split('-')
# print(minus_str)

fr = sum(map(int, minus_str[0].split('+')))
# print("1",fr)

for i in range(1, len(minus_str)):
    if minus_str[i].isdigit():
        fr-=int(minus_str[i])

    else:
        plus_str = list(map(int, minus_str[i].split('+')))
        # print("2", plus_str)
        fr-= sum(plus_str)
        # print("3",fr)

print(fr)