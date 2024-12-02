# You are given an array of size ‘n’ to find the minimum number of steps to either convert it into either non-decreasing or non-increasing array. In one step you can either increment or decrement the element of the array.

def minimum_cost(array):
    
    n=len(array)
    
    non_decreasing=sorted(array)
    
    non_increasing= sorted(array,reverse=True)

    cost_non_decrease=0
    
    for i in range(n):
        
        cost_non_decrease += abs(array[i]-non_decreasing[i])

    
    cost_non_increase=0
    for i in range(n):
        
        cost_non_increase += abs(array[i] - non_increasing[i])

    
    return min(cost_non_decrease,cost_non_increase)

print(minimum_cost([3 ,1 ,3 ,1]))

    