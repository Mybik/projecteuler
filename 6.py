'''The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

sum_of_the_squares = 0
the_square_of_the_sum = 0
for x in range(101):
    the_square_of_the_sum += x
    sum_of_the_squares += x ** 2

print(sum_of_the_squares)
print(the_square_of_the_sum**2)
answer = sum_of_the_squares - (the_square_of_the_sum)**2
print(answer)