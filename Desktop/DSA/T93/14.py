#maximum sum circular subarray 

def main(array:list[int])->int:
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n):
        
        current=0
        
        for j in range(i,i+n):
            
            current += array[j%n]
            
            if current < 0:
                
                current = 0
                
            maximum=max(maximum,current)

    return maximum

arr = [1, 2, -3, -4, 5]
print(main(arr))