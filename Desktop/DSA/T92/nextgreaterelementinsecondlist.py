# You are given an array ‘A’ containing a permutation ‘N’ numbers (0 ≤ A[i] < N). You are also given another array ‘B’ containing a permutation ‘M’ numbers (0 ≤ B[j] < M) and it is also given that N ≤ M.

# For each element in array ‘A’ you need to find the first greater element to the right of the element in array ‘B’ that has the same value as the current array A’s element. In other words, for each ‘i’ from 0 to N - 1 in array ‘A’, you need to find an index ‘j’ in array ‘B’ such that A[i] = B[j], now you need to print the element that lies on the right of the j’th index and is also greater than B[j]. Print -1 if there is no greater element.

def next_greater_element_in_second_array(array1:list[int],array2:list[int])->list[int]:
    
    n=len(array1)
    m=len(array2)

    result=[]


    for i in range(n):
        
        found=False
        
        for j in range(m):
            
            if array1[i] ==  array2[j]:
                
                for k in range(j+1,m):
                    
                    if array2[k]>array2[j]:
                        
                        result.append(array2[k])
                        found=True
                        break
                
                if not found:
                    
                    result.append(-1)
                    
                break
                
    return result

A = [2, 3, 1]
B = [1, 2, 3, 4]

print(next_greater_element_in_second_array(A,B))

