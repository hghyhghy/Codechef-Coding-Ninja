

#return duplicates 

def main(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num]=1
            
    
    duplicates=sorted([num for num,count in freq.items() if count ==2])

    return duplicates

nums = [4, 3, 2, 7, 8, 2, 1, 4]
print(main(nums))