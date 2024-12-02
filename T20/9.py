

# # You are given an integer array 'ARR' of size 'N' and an integer 'S'. Your task is to return the list of all pairs of elements such that each sum of elements of each pair equals 'S'.

# Note:

# Each pair should be sorted i.e the first value should be less than or equals to the second value. 

# Return the list of pairs sorted in non-decreasing order of their first value. In case if two pairs have the same first value, the pair with a smaller second value should come first.

def find_pair_with_given_sum(arr,n,s):

    arr.sort()
    store=[]

    left=0
    right=n-1

    while left < right:

        pair_sum= arr[left] + arr[right]

        if  pair_sum ==  s:

            store.append((arr[left],arr[right]))

            left += 1
            right -=1 

        elif pair_sum < s:

            left += 1

        else:

            right -= 1

    return store

ARR = [1, 5, 7, -1, 5]
N = len(ARR)
S = 6

print(find_pair_with_given_sum(ARR,N,S))