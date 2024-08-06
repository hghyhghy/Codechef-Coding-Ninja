# 4 Sum | Find Quads that add up to a target value


# 53

# 1
# Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.

def four_sum(arr):
    
    n=len(arr)
    stack=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            for  k in range(j+1,n):
                
                for l in range(k+1,n):
                    
                    if (arr[i]+arr[j]+arr[k]+arr[l]) == 0:
                        
                        stack.append([arr[i],arr[j],arr[k],arr[l]])

    return stack

arr=[1,0,-1,0,-2,2]
print(four_sum(arr))