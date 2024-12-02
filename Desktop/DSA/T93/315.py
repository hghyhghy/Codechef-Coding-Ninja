

#majority element

def main(array):
    
    freq={}
    n=len(array)

    for num in array:
        
        if num in freq:
            
            freq[num] +=1
            
        else:
            
            freq[num] =1
            
    limit =n//3
    
    majority=[num for num,count in freq.items() if count > limit]
    
    return majority

nums = [3, 2, 3]
print(main(nums))