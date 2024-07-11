def sum_cycle(n):
    a = n//10
    b = n % 10
    c = (a+b)%10
    
    new_n = 10 * b + c
    
    return new_n

n = int(input())
org_n = n
cycle = 0

while True:
    new_n = sum_cycle(n)
    cycle +=1
    
    if org_n == new_n:
        break
    
    n = new_n
print(cycle)

    