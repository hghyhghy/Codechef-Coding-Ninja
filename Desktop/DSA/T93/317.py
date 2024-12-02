

#duplicates 

def main(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] =1
            
    
    for num,count in freq.items():
        
        if count > 1:
            
            return num
        
    return 0

nums = [1,3,4,2,2]
print(main(nums))