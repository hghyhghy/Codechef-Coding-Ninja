
#kadanes algorithm 

def main(array:list[int])->int:
    
    current=0
    max_sum=float("-inf")

    for num in  array:
        
        current += num
        
        if current > max_sum:
            
            max_sum = current
            
        if current <0:
            
            current = 0
            
    return  max_sum

arr=list(map(int,input().split()))
print(main(arr))