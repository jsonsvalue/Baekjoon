def fibo_dp(n):
    fibo_dict = {}
    
    for i in range(n+1):
        if i ==0 or i==1:
            fibo_dict[i] = i
            
        else:
            if i not in fibo_dict:
                fibo_dict[i] = fibo_dict[i-1] + fibo_dict[i-2]
        
    return fibo_dict[n]

n = int(input())
print(fibo_dp(n))
    
        