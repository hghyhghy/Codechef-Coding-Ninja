#best time buy sell stock
def main(array,fee):

    minimum=float("inf")
    maximum=0
    
    for num in array:
        
        minimum=min(minimum,num)

        profit = (num-minimum)+fee
        
        if profit >maximum:
            
            maximum=profit
            
    return maximum

n=int(input("Enter fees"))
arr=list(map(int,input().split()))

print(main(arr,n))