

#single element

def func(array):

    freq={}

    for num in array:

        if num in freq:

            freq[num] +=1

        else:

            freq[num] = 1


    single=[num for num,count in freq.items() if count ==1]

    return  single

nums = [2, 2, 1, 3, 3]
print(func(nums))