# Problem statement
# Selection sort is one of the sorting algorithms that works by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning of the unsorted region of the array.

# You are given an unsorted array consisting of N non-negative integers. Your task is to sort the array in non-decreasing order using the Selection Sort algorithm.

def selection_sort(arrat:list[int])->list[int]:
    
    n=len(arrat)
    
    for i in range(n):
        
        minimum = i
        
        for j in range(i+1,n):
            
            if arrat[j] < arrat[minimum]:
                
                minimum =j
                
        
        arrat[i],arrat[minimum] = arrat[minimum],arrat[i]
        
    
    return arrat

arr = [64, 25, 12, 22, 11] 
print(selection_sort(arr))