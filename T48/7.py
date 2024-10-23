# Ninja just got an offer letter from a reputable company. The company sent him an offer letter along with the salary bifurcation.

# In that bifurcation,Total Salary was not mentioned but instead a ‘basicSalary’ and an upper case character representing grade was mentioned, depending on which the Total Salary is calculated.

# Help Ninja in calculating his total salary, where total salary is defined as:

# ‘totalSalary’ = ‘basic’ + ‘hra’ + ‘da’ + ‘allowance’ - ‘pf’
# The above terms are as follows:

# ‘hra’ = 20% of ‘basic’
# ‘da’ = 50% of ‘basic’
# ‘allowance’ = 1700 if grade = ‘A’
# ‘allowance’ = 1500 if grade = ‘B’
# ‘allowance’ = 1300 if grade = ‘C' or any other character
# ‘pf’ = 11% of ‘basic’.

def total_salary(basic,grade):
    
    hra=0.20 * basic
    da=0.50 * basic
    pf =0.11 *basic
    
    if grade == "A":
        
        allowance= 1700
        
    elif grade == "B":
        
        allowance = 1500
        
    else:
        
        allowance = 1300
        
    total = basic + hra + da + allowance - pf
    
    return total

basicSalary = 10000
grade = 'A'
print(total_salary(basicSalary,grade))
    
    