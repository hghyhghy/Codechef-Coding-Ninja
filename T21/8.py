

# sum of two array elements

def two_sum_array(a1,a2):

    if len(a1) != len(a2):

        return 0
    
    p1,p2=0,0
    result = []

    while  p1<len(a1) and p2<len(a2):

        result.append([a1[p1] + a2[p2]])
        p1 += 1
        p2 += 1

    return result

array1 = [1, 2, 3, 4, 5]
array2 = [10, 20, 30, 40, 50]

print(two_sum_array(array1,array2))