# Merge two sorted arrays without extra space

def merge_sorted_arrays(a1,a2):
    
    m=len(a1)-len(a2)
    n=len(a2)

    i=m-1
    j=n-1
    k=m+n-1
    
    while i >= 0 and j >= 0:
        
        if a1[i] > a2[j]:
            
            a1[k] = a1[i]

            i -=1
            
        else:
            
            a1[k] = a2[j]
            j -= 1
            
        k -= 1
        
    while j>=0:
        
        a1[k] = a2[j]
        j -= 1
        k -= 1
    
    return a1

arr1 = [1, 3, 5,0,0,0]  # Assume 0s are placeholders for extra space
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1,arr2))