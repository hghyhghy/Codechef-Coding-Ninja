# check whather a number is an armstrong number 

def is_armstrong(num):
    
    str_num=str(num)
    lenght= len(str_num)

    check_number=sum(int(digit) ** lenght for digit in str_num)

    return check_number == num

print(is_armstrong(153))