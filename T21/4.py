
# remove duplicates from an unsorted array

def remove_duplicates(arr):

    seen={}
    store=[]

    for num in arr:

        if num not in seen:

            seen[num] = True
            store.append(num)

    return store

sorted_array = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(sorted_array))