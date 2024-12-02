
#sort zero and  one

def main(array:list[int])->list[int]:
    
    zero=array.count(0)
    one=len(array)-zero
    
    array[:zero]=[0]*zero
    array[zero:]=[1]*one
    
    return array

arr=list(map(int,input().split()))
print(main(arr))