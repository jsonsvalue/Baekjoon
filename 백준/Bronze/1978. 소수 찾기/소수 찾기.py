import math 

tot_num = int(input())
tot_num_list = list(map(int,input().split()))

tot_count = 0
count = 0

for i in range(tot_num):
    num = tot_num_list[i]
    
    if num < 2 :
        continue
    
    is_prime = True
    for k in range(2, int(math.sqrt(num)) +1):
        if num % k == 0:
            is_prime = False
            break
            
    if is_prime:
        count+=1
        
tot_count+=count

print(tot_count)        
