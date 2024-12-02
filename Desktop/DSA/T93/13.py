#kadanes algorithm

def main(array:list[int])->int:
    
    maximum=float("-inf")
    total=0
    
    for  num in array:
        
        total += num
        
        if total > maximum:
            
            maximum = total
            
        
        if total <0:
            
            total = 0
            
    return maximum

ARR = [1, 2, -3, 4, 5]
print(main(ARR))