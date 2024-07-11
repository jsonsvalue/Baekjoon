def sum_cycle(n_str):
    
    if len(n_str)<2:
        n_str = '0' + n_str

    new_n_str = ''

    fr, bk = int(n_str[0]), int(n_str[1]) 
    fr_str, bk_str = n_str[0], n_str[1]

    if fr + bk >= 10:
        new_bk_str = str( fr + bk)[1]
    else:
        new_bk_str = str( fr + bk )

    new_n_str = bk_str + new_bk_str
    
    return new_n_str


n_str = input()
if len(n_str) < 2:
    n_str = '0' + n_str

org_n_str = n_str
cycle = 0
while True:
    new_n_str = sum_cycle(n_str)
    cycle+=1                                                                                                                                                        
    if new_n_str == org_n_str:
        break
    n_str = new_n_str
    
print(cycle)


'''
while n_str != sum_cycle(n_str):
    n_str = sum_cycle(n_str)
    sum_cycle(n_str)
    
    cycle+=1
    if n_str == sum_cycle(n_str):
        break
'''



