
#subarray sum equal k
def main(array,target):

    n=len(array)
    count=0

    for i in range(n):

        curr = 0

        for j in range(i,n):

            curr += array[j]

            if curr == target:

                count +=1

    return  count

nums = [1,1,1]
k = 2
print(main(nums,k))