from dns.rrset import from_rdata


#single number

def func(array):

    freq={}
    for num in array:

        if num in freq:

            freq[num] +=1

        else:

            freq[num]  =1


    r=[]
    for num,count in freq.items():

        if count  == 1:

            r.append(num)

    return  r

arr = [2, 3, 7, 9, 11, 2, 3, 11]
print(func(arr))