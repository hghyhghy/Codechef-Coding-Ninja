# Problem statement
# You are given an array “ARR” of size N. Your task is to find out the sum of maximum and minimum elements in the array.

# Follow Up:
# Can you do the above task in a minimum number of comparisons?

def sum_of_max_min(array:list[int])->int:
    
    n=len(array)
    
    def bubble_sort(array):
        
        for i in range(n):
            
            for j in range(0,n-i-1):
                
                if array[j]>array[j+1]:
                    
                    array[j],array[j+1] =  array[j+1],array[j]
        
        return array
    
    temp=bubble_sort(array)
    
    return temp[0]+temp[len(temp)-1]

arr = [3, 5, 1, 9, 2]
print(sum_of_max_min(arr))
    
    
        
        