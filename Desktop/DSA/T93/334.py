


#peak element

def function(array):

    peak = array[0]
    for i in range(len(array)-1):

        if array[i] > peak:

            peak=array[i]

    return  peak

nums = [1,2,3,1]
print(function(nums))