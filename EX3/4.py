# Python program explaining 
# numpy.random.random_integers() function 

# importing numpy 
import numpy as geek 

# output array 
out_arr = geek.random.random_integers(low = 0, high = 5, size = 4) 
print ("Output 1D Array filled with random integers : ", out_arr) 

out_arr = geek.random.random_integers(low = 3, size =(3, 3)) 
print ("Output 2D Array filled with random integers : ", out_arr)  