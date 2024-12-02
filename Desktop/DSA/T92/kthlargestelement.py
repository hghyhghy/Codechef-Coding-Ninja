# Problem statement
# Ninja loves playing with numbers. One day Alice gives him some numbers and asks him to find the Kth largest value among them.

def kth_largest(nums:list[int],k:int)->int:
    
    def quick_sort(num):
        
        if len(num) <=1:
            
            return num
        
        else:
            
            mid=num[len(num)//2]
            left=[x for x in num if x >mid]
            middle=[x for x in num if x==mid]
            right=[x for x in num if x<mid]
            
            return quick_sort(left)+middle+quick_sort(right)

    
    
    sorted_array=quick_sort(nums)

    return sorted_array[k-1]

nums = [3, 2, 1, 5, 6, 4]
k = 2

print(kth_largest(nums,k))