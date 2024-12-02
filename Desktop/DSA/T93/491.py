

def main(a1,a2):

    seen1=set(a1)
    seen2=set(a2)

    common = seen1.intersection(seen2)
    distinct = seen1.union(seen2)

    return  len(common),len(distinct)

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8]

print(main(arr1,arr2))