import math

tot_num = int(input())

def is_prime (num):
    if num < 2 :
        return False

    for i in range(2, int(math.sqrt(num)) + 1 ):
        if num % i == 0:
            return False

    return True        


fin_gold_list = []


#주어진 데이터 개수에 따른 반복
for i in range(tot_num):
    num = int(input())
    gold_list = []

    
    #골드바흐 목록 확인 
    is_gold = True
    for j in range( num //2 + 1 ):
        if is_prime(j):
            oth_num = num - j
            
            if is_prime(oth_num)==False:
                is_gold = False

            if is_prime(oth_num)==True:                
                gold_list.append([j, oth_num])

    diff = float('inf')
    diff_idx = -1

    for k in range(len(gold_list)):
        j, oth_num = gold_list[k]
        giv_diff = abs(j - oth_num)

        if giv_diff < diff:
            diff = giv_diff
            diff_idx = k

    if diff_idx != -1:
        fin_gold_list.append(gold_list[diff_idx])

    

for i in range(len(fin_gold_list)):
    for j in range(len(fin_gold_list[i])):
        print(fin_gold_list[i][j])