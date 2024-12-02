# Left shift, Right shift
# Left shift
# Left-shifting a binary number involves moving its bits to the left by a specified number of positions.

# In most of the languages, the left shift operator (<<) is used for this operation. The syntax is:

def left_and_right_shift(number,right,left):
    
    right_shift=number >> right
    
    left_shift = right_shift << left
    
    return right_shift,left_shift

number = 7
right_shift_positions = 2
left_shift_positions = 2

right_shift_result, left_shift_result = left_and_right_shift(number, right_shift_positions, left_shift_positions)

print(f"Right shift result: {right_shift_result}")  # Output: 1
print(f"Left shift result: {left_shift_result}")    # Output: 4