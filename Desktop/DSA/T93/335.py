

#merge two list

def function(num1,m,num2,n):

    i=m-1
    j=n-1
    k=m+n-1

    while i>=0 and j>=0:

        if num1[i]>num2[j]:

            num1[k]= num1[i]
            i -=1

        else:

            num1[k]=num1[j]
            j -=1

        k -=1

    while j >=0:

        num1[k]=num2[j]
        j -=1
        k -=1

    return  num1

nums1 = [1, 2, 3, 0, 0, 0]  # The last 0s are placeholders for nums2
m = 3  # Number of elements initially in nums1
nums2 = [2, 5, 6]
n = 3

print(function(nums1,m,nums2,n))
