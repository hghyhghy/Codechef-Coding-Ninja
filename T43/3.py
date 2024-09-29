# dupliactes in the array

def finding_duplicates(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
            
    result=[num  for num,count in freq.items() if count > 1]

    return result

arr = [1, 2, 3, 4, 2, 3, 5, 6]
print(finding_duplicates(arr))