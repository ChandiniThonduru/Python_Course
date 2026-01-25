"""
Count number of digits in a number
"""
num = int(input("Enter integer: "))
digits = 0
while num > 0:
    digits += 1
    num = num // 10
print("number of digits", digits)

"""
Reverse a number using loop
"""
num1 = int(input("Enter integer: "))
rev = 0
while num1 > 0:
    rev = (rev * 10) + (num1 % 10)
    num1 = num1 // 10
print("reverse of a number : ", rev)

"""
Print Fibonacci series
"""
num2 = int(input("Enter a nuber to generate Fibonacci series: "))
a, b = 0, 1
for i in range(0, num2):
    print(a, end=" ")
    a, b = b, a + b

"""
Check whether a number is prime

Input: 11
Output: Prime
"""
num3 = int(input("Enter number to check prime or not: "))
is_prime = True
for i in range(2, (num3 // 2)+1):
    if num3 % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("Not Prime")

"""
Print star pattern

Input: 4
Output:

*
**
***
****
"""
num4 = int(input("Enter a number to print star pattern: "))
for i in range(1, num4 + 1):
    print("*" * i)
"""solution2"""
for i in range(num4):
    for j in range(i + 1):
        print("*", end="")
    print()