

#majority element

def  function(array):

    freq={}
    n=len(array)

    for num in array:

        if num in freq:

            freq[num] +=1

        else:

            freq[num] =1


    limit=n//2

    majority=[num for num,count in freq.items() if count > limit]

    return  majority

nums = [2,2,1,1,1,2,2]
print(function(nums))