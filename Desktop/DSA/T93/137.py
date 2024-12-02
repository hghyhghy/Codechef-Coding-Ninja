

#common elements

def main(arr1,arr2):
    
    set1=set(arr1)
    set2=set(arr2)

    common  =  set1.intersection(set2)

    return common

array1 = ["apple", "banana", "cherry", "date"]
array2 = ["banana", "date", "fig", "grape"]

print(main(array1,array2))