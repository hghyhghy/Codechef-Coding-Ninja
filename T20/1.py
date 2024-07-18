
# first element to occur k times 

def first_element_to_occur_k_times(arr,k):

    count={}

    store=[]

    for num in arr:

        if num  in count:

            count[num] += 1

        else:

            count[num] = 1

            store.append(num)

        
        if count[num] ==  k:

            return num
    

    return None

arr = [1, 2, 3, 2, 1, 2, 3, 1]
k = 3

print(first_element_to_occur_k_times(arr,k))

