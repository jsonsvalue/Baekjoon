def big_mod(a, b, c):
    if b==1:
        return a%c
    elif b % 2 ==0:
        return (big_mod(a, b//2, c) ** 2) %c
    else:
        return (big_mod(a, b//2, c) **2 * a) %c

a, b, c =list(map(int, input().split()))

print(big_mod(a,b,c))
