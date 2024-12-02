# Find common elements in three sorted arrays
# Last Updated : 05 Jul, 2024
# Given three sorted arrays in non-decreasing order, print all common elements in these arrays.

# Note: In case of duplicate common elements, print only once.

# Examples: 

# Input: A[] = {1, 5, 10, 20, 30} , B[] = {5, 13, 15, 20}, C[] = {5, 20} 
# Output: 5 20
# Explanation: 5 and 20 are common in all the arrays.

# Input: A[] = {1, 5, 10, 20, 30}, B[] = {5, 13, 15, 20}, C[] = {5, 20} 
# Output: 5
# Explanation: 5 occurs multiple times in all the three arrays but it will be printed once.

def common_in_three_sorted_array(arr1,arr2,arr3):
    
    p1=p2=p3=0
    common=set()

    while p1<len(arr1) and p2<len(arr2) and p3<len(arr3):
        
        if arr1[p1] == arr2[p2] ==arr3[p3]:
            
            common.add(arr1[p1])

            p1 += 1
            p2 += 1
            p3 += 1
            
        elif arr1[p1] < arr2[p2]:
            
            p1 += 1

        elif arr2[p2] < arr3[p3]:
            
            p2 += 1
            
        else:
            
            p3 += 1
            
    return sorted(common)

A = [1, 5, 10, 20, 30]
B = [5, 13, 15, 20]
C = [5, 20]

print(common_in_three_sorted_array(A,B,C))



