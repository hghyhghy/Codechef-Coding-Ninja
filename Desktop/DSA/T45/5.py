# sort the numbers by frequency 

def sort_by_frequency(array):
    
    freq={}
    if not array or len(array) <=1:
        
        return array
    
    for num in array:
        
        if num in freq:

            freq[num] += 1
            
        else:
            freq[num] = 1
            
    sorted_version=sorted(freq.items() ,key=lambda x: (x[1],x[0]))

    sorted_version.reverse()
    store=[]

    for num,count in sorted_version:
        
        store.extend([num]*count)

    return store

arr = [4, 5, 6, 5, 4, 3]
print(sort_by_frequency(arr))
            