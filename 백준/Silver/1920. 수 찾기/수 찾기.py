n = int(input())
giv_string = list(map(int, input().split()))

m = int(input())
key_string = list(map(int, input().split()))

giv_string.sort()

for i in range(m):
    pl = 0
    pr = n-1
    isExist = False
    
    while True:
        pc = (pl+pr)//2
        if giv_string[pc] == key_string[i]:
            isExist = True
            print(1)
            break
        elif giv_string[pc] < key_string[i]:
            pl = pc + 1
        else:
            pr = pc -1
        if pl > pr:
            break
    
    if not isExist:
        print(0)

        
        


        