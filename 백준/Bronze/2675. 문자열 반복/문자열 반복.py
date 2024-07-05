tot_num = int(input())

for i in range(0, tot_num):
    tot_char_list = input().split()
    
    giv_int, giv_char = int(tot_char_list[0]), tot_char_list[1]
    
    for j in range(0, len(giv_char)):
        for k in range(0, giv_int):
            print(giv_char[j], end = "")
    print()
            