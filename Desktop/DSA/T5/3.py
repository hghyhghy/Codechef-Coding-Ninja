# bubble sort implementation 

def bubble_sorting(arr):
    
    n=len(arr)

    for i in range(n):
        
        for j in range(n-1-i):
            
            if arr[j] > arr[j+1]:
                
                arr[j],arr[j+1] =  arr[j+1],arr[j]

    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sorting(arr))