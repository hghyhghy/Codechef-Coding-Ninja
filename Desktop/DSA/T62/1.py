# Problem statement
# You are given an array/list ARR consisting of N integers. Your task is to find all the distinct triplets present in the array which adds up to a given number K.

# An array is said to have a triplet {ARR[i], ARR[j], ARR[k]} with sum = 'K' if there exists three indices i, j and k such that i!=j, j!=k and i!=j and ARR[i] + ARR[j] + ARR[k] = 'K'.

def three_sum_main(array,target):
    
    n=len(array)
    result=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if (array[i]+array[j]+array[k])==target:
                    
                    result.append([array[i],array[j],array[k]])
    return result

nums = [-1, 0, 1, 2, -1, -4]
n=0

print(three_sum_main(nums,n))