# def hanoi(n, start, aux, dest)

def hanoi(n, a, b, c):
    if n == 1:
        print(f"{a} {c}")
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)
    
n = int(input())

print(2**n - 1)
if n <= 20:
    hanoi(n, 1, 2, 3)

    