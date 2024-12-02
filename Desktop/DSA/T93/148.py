
#maximum difference

def main(array:list[int])->int:
    
    array.sort(reverse=True)

    return array[0]-array[len(array)-1]

nums=list(map(int,input().split()))
print(main(nums))