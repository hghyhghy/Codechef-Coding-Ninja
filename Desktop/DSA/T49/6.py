# You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. You need to print their intersection; An intersection for this problem can be defined when both the arrays/lists contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.

# Note :
# Input arrays/lists can contain duplicate elements.

# The intersection elements printed would be in the order they appear in the first array/list(ARR1)

def intersection(arr1,arr2):
    
    arr1.sort()
    arr2.sort()

    i=0
    j=0
    intersection=[]

    while i < len(arr1) and j< len(arr2):
        
        if arr1[i] ==  arr2[j]:
            
            intersection.append(arr1[i])

            i+= 1
            j += 1
            
        elif arr1[i] < arr2[j]:
            
            i += 1
            
        else:
            
            j+=1
            
    return intersection

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5]
print(intersection(arr1,arr2))