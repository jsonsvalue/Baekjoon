dwrf_list = []
for i in range(9):
    dwrf = int(input())
    dwrf_list.append(dwrf)

#dwrf_list.sort()


fin_dwrf_list = []
tot_hght = 0
dwf_idx1 = -1
dwf_idx2 = -1

for i in range(9):
    tot_hght += dwrf_list[i]

found_match = False
for i in range(9):
    for j in range(i+1,9):
        if dwrf_list[i] + dwrf_list[j] == tot_hght - 100:
            found_match = True
            dwrf_list.remove(dwrf_list[j])
            dwrf_list.remove(dwrf_list[i])
            break
    #이미 위에서 for 문을 빠져나왔는데, 또 빠져나와야할까?
    if found_match:
        break


dwrf_list.sort()
print(*dwrf_list, sep = "\n")    