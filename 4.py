
'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

palindromic_numbers = []
for i in range(100, 1000):
    i *= i
    number = str(i)
    reversed_number = number[::-1]
    if reversed_number == number:
        palindromic_numbers.append(number)
print(palindromic_numbers[-1])