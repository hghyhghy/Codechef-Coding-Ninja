

#rotation

def rotation(arr,start,end):

    while start < end:

        arr[start],arr[end]=arr[end],arr[start]
        start +=1

        end -=1

def function(arr,k):

    n=len(arr)
    k =k % n


    rotation(arr,0,n-1)

    rotation(arr,k,n-1)

    rotation(arr,0,k-1)

    return  arr


nums = [1,2,3,4,5,6,7]
k = 3

print(function(nums,k))

