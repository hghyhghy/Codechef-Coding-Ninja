# largest element from an array 

def largest_element(array):
    
    largest_element1=array[0]

    for i in range(len(array)):
        
        if array[i] > largest_element1:
            
            largest_element1 =  array[i]

    return largest_element1

arr=[4,1,3,10,9,8,6]
print(largest_element(arr))