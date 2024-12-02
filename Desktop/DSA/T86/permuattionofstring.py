# Problem statement
# You are given a string 'STR' consisting of lowercase English letters. Your task is to return all permutations of the given string in lexicographically increasing order.

# String A is lexicographically less than string B, if either A is a prefix of B (and A ≠ B), or there exists such i (1 <= i <= min(|A|, |B|)), that A[i] < B[i], and for any j (1 <= j < i) A[i] = B[i]. Here |A| denotes the length of the string A.

# For example :

# If the string is “bca”, then its permutations in lexicographically increasing order are { “abc”, “acb”, “bac”, “bca”, “cab”, “cba” }.

from itertools import permutations

def permutation_of_string(string):
    
    perm =permutations(string)

    main_result ={"".join(p) for p  in perm}

    sorted_result=sorted(main_result)

    return sorted_result

string = "bca"
print(permutation_of_string(string))