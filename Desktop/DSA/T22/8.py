# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

def maximum_product(array):
    
    array.sort()

    max_product=0
    for i in range(len(array)):
        
        for j in range(i+1,len(array)):
            
            product= array[i]*array[j]

            max_product = max(max_product,product)

    return max_product

nums = [3,4,5,2]
print(maximum_product(nums))