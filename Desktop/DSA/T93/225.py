

#maximizing array sum

def main(arr1,arr2):
    
    arr1.sort()
    arr2.sort(reverse=True)
    n=len(arr1)
    
    i=j=0
    
    while  i<n and j<n:
        
        if arr2[j] > arr1[i]:
            
            arr1[i]=arr2[j]

            i +=1
            
        j +=1
        
    return sum(arr1)

nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]

print(main(nums1,nums2))

