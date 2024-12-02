

#minimum size subarray

def  function(array,target):

    n=len(array)
    minimum=float("inf")

    for i in range(n):

        curr= 0

        for j in range(i,n):

            curr += array[j]

            if curr >= target:

                minimum=min(minimum,j-i+1)

    return  minimum


nums = [2,3,1,2,4,3]
t=7

print(function(nums,t))

