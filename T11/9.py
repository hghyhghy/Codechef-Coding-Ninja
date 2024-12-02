#  Bastin once had trouble finding the numbers in a string. The numbers are distributed in a string across various test cases. There are various numbers in each test case you need to find the number in each test case. Each test case has various numbers in sequence. You need to find only those numbers which do not contain 9. For eg, if the string contains "hello this is alpha 5051 and 9475".You will extract 5051 and not 9475. You need only those numbers which are consecutive and you need to help him find the numbers. Print the largest number.

import re

def finding_max_without_nine(string):
    
    numbers = re.findall(r'\b\d+\b',string)

    temp_numbers=[int(num) for num in numbers if '9' not in num]

    if temp_numbers:
        
        maximum=max(temp_numbers)
        return maximum
    else:
        
        return "NO maximum numbers"

input_string = "hello this is alpha 5051 and 9475"
result = finding_max_without_nine(input_string)
print(result)