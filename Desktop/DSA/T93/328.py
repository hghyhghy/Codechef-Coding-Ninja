

#kth pair with smallest sum

def main(array1,array2,k):

    store=[]
    for num in array1:

        for num1 in array2:

            store.append([num,num1])

    store.sort(key=lambda  x:x[0]+x[1])

    return  store[:k]

nums1 = [1, 7]
nums2 = [3, 5]
k = 3

print(main(nums1,nums2,k))