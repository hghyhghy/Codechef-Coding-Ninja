

#sorted array

def main(array):

    if len(array) <=1:

        return  array

    else:

        mid=array[len(array)//2]
        left=[x for x in array if x <mid]
        middle=[x for x in array if x == mid]
        right=[x for x in array if x>mid]

        return main(left) + middle + main(right)

nums = [5,2,3,1]
print(main(nums))