# You are given three arrays X, Y and Z of size A,B and C respectively.Also, all three arrays are sorted in non-decreasing order. Find i, j, k such that : 0 <= i < A, 0 <= j < B, 0 <= k < C and max(abs(X[i] - Y[j]), abs(Y[j] - Z[k]), abs(Z[k] - X[i])) is minimized. Your task is to return the minimum of all the max(abs(X[i] - Y[j]), abs(Y[j] - Z[k]), abs(Z[k] - X[i]))

# Note:
# 1. All the arrays are sorted in non-decreasing order.
# 2. abs(x) denotes the absolute value of x, i.e. if x<0, the abs function returns (-x) so that the final value of x becomes positive.

def minimize_absolute_difference(x,y,z):
    
    a=len(x)
    b=len(y)
    c=len(z)
   
    minimum =float("inf")

    for i in range(a):
        
        for j in range(b):
            
            for k in range(c):
                
                diff1=abs(x[i]-y[j])

                diff2=abs(y[j]-z[k])
                
                diff3=abs(z[k]-x[i])

                
                current = max(diff1,diff2,diff3)

                minimum = min(minimum,current)

    
    return minimum

X = [1, 4, 10]
Y = [2, 15, 20]
Z = [10, 12]
print(minimize_absolute_difference(X,Y,Z))