# Problem statement
# Ninja has been given two sorted integer arrays/lists ‘ARR1’ and ‘ARR2’ of size ‘M’ and ‘N’. Ninja has to merge these sorted arrays/lists into ‘ARR1’ as one sorted array. You may have to assume that ‘ARR1’ has a size equal to ‘M’ + ‘N’ such that ‘ARR1’ has enough space to add all the elements of ‘ARR2’ in ‘ARR1’.

# For example:

# ‘ARR1’ = [3 6 9 0 0]
# ‘ARR2’ = [4 10]
# After merging the ‘ARR1’ and ‘ARR2’ in ‘ARR1’. 
# ‘ARR1’ = [3 4 6 9 10]

def merge_two_sorted_list(ar1,ar2):
    
    i=0
    j=0
    
    merged_list=[]

    while i<len(ar1) and j<len(ar2):
        
        if ar1[i] < ar2[j]:
            
            merged_list.append(ar1[i])

            i += 1
            
        else:
            
            merged_list.append(ar2[j])

            j += 1
            
    
    while  i<len(ar1):
        
        merged_list.append(ar1[i])
        i+=1

    while j <len(ar2):
        
        merged_list.append(ar2[j])
        j+=1
    
    return merged_list


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print(merge_two_sorted_list(arr1,arr2))
        
        