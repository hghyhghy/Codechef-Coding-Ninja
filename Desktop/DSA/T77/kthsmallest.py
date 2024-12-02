# You are given an array of integers 'ARR' of size 'N' and another integer 'K'.



# Your task is to find and return 'K'th smallest value present in the array.



# Note: All the elements in the array are distinct. 

def bubble_sort(array:list[int])->list[int]:
    
    n=len(array)
    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j]>array[j+1]:
                
                array[j],array[j+1]=array[j+1],array[j]
                
    return array

def main(array:list[int],k:int)->int:
    
    temp =  bubble_sort(array)
    
    return temp[k-1]

arr = [12, 3, 5, 7, 19]
print(main(arr,2))