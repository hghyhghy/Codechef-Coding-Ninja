# sorting the array by frequency 

def sort_by_frequecny(arr):
    
    freq={}

    for num in arr:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    freq_list=[(item,freq) for item,freq in freq.items()]

    freq_list.sort(key=lambda x:x[1])
    
    temp =[]

    for item,freq in freq_list:
        
        temp.extend([item] * freq)

    return temp

arr = [4, 1, 2, 2, 3, 4, 4, 1, 2]
print(sort_by_frequecny(arr))