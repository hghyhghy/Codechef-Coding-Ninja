# Merge two Sorted Arrays Without Extra Space


# 90

# 6
# Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

def merge_two_sorted(a1,a2):
    
    a1.sort()
    a2.sort()
    n=len(a1)
    m=len(a2)

    arr1.extend([0]*m)
    
    l=n-1
    i=m-1
    k=n+m-1
    
    while l>=0  and i >= 0:
        
        if a1[l] > a2[i]:
            
            arr1[k] = arr1[l]
            l -=1
        else:
            
            arr1[k] = a2[i]
            i -= 1
            
        k -= 1
        
    while i >=0:
        
        arr1[k] =  a2[i]
        i -= 1
        k -= 1
    
    
    return arr1

arr1 = [1, 5, 9]
arr2 = [2, 3, 7, 11]
print(merge_two_sorted(arr1,arr2))
        
        
            
    
        
        