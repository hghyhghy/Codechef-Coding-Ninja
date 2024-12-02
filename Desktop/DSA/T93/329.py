


#kth largest element

def main(array,k):

    def quick(array):

        if len(array)<=1:

            return  array

        else:

            mid=array[len(array)//2]
            left=[x for x in array if x>mid]
            middle=[x for x in array if x == mid]
            right=[x for x in array if x<mid]

            return  quick(left)+middle+quick(right)




    temp=quick(array)
    return  temp[k-1]

nums = [3,2,1,5,6,4]
k = 2

print(main(nums,k))