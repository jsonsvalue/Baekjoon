n = int(input())

tile_dic = {}

for i in range(n+1):
    if i == 0 :
        tile_dic[i] = 1
    
    elif i == 1:
        tile_dic[i] = 1
    
    else:
        if i not in tile_dic:
            tile_dic[i] = (tile_dic[i-1] + tile_dic[i-2])%15746

print(tile_dic[n])



            
            