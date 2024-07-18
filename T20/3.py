

# move all zeroes to the end of the array 

def move_all_zeroes_to_the_end(arr):

    positions=0

    for i in range(len(arr)):

        if arr[i] != 0:

            arr[positions] = arr[i]
            positions += 1

    
    for i in range(positions,len(arr)):

        arr[i] = 0

    return arr
arr = [0, 1, 0, 3, 12]
print(move_all_zeroes_to_the_end(arr))