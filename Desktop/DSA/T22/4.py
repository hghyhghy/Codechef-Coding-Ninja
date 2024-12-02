# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import Counter

def k_most_frequent_elements(nums,k):
    
    counting= Counter(nums)

    temp_counter =sorted(counting.items(), key= lambda x : x[1], reverse=True)

    k_frequent = [ element for element ,fre in temp_counter[:k]]

    return k_frequent

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(k_most_frequent_elements(nums,k))