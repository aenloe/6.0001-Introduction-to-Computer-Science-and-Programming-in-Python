#naive attempt
#difference between sum of squares and square of sums
def sum_square_difference(x):
    sum_of_squares = 0
    for i in range(1,x+1):
        sum_of_squares = sum_of_squares + (i ** 2)
    
    square_of_sums = 0
    for i in range(1,x+1):
        square_of_sums = square_of_sums + i
    square_of_sums = square_of_sums ** 2
    
    difference = abs(square_of_sums - sum_of_squares)
    return difference

print(sum_square_difference(10))
print(sum_square_difference(100))