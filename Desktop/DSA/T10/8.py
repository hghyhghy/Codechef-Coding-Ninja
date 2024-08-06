# K most frequent elements

from collections import defaultdict

def kth_frequent_elements(array,k):
    
    freq=defaultdict(int)
    for num in array:
        
        freq[num] += 1
        
    freq_list=[(key,value) for key,value in freq.items()]

    freq_list.sort(key=lambda x : x[1], reverse=True)

    kth_element=[element for element,freq in freq_list[:k]]

    return kth_element

arr = [1, 3, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
k = 3

print(kth_frequent_elements(arr,k))
