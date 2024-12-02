
#best time to buy and sell  stock 

def main(array:list[int])->int:
    
    n=len(array)
    max_profit=0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            profit = array[j] - array[i]

            if profit  > max_profit:
                
                max_profit = profit
                
    return max_profit


nums=list(map(int,input().split()))
print(main(nums))