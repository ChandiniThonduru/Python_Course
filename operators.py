"""
1️⃣ Take two numbers and perform all arithmetic operations
"""
import ast

a = 10
b = 3

print("Addition", a + b)   # Addition
print("Subtraction", a - b)   # Subtraction
print("Multiplication", a * b)   # Multiplication
print("Division", a / b)   # Division
print("Floor Division", a // b)  # Floor Division
print("Modulus", a % b)   # Modulus
print("Power", a ** b)  # Power
"""
2️⃣ Check whether a number is positive, negative, or zero
"""
num = 2
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")
"""
3️⃣ Check if a number is divisible by both 3 and 5
"""
if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by both 3 and 5")
"""
4️⃣ Compare two numbers and print the largest
"""
num1 = 2
num2 = 5
if num1 > num2:
    print(num1, " is largest")
else:
    print(num2, " is largest")
"""
5️⃣ Check if a character exists in a string
"""
my_str = "ChandiniAutomationEngineer"
if 'C' in my_str:
    print("Character in my_str")
"""
6️⃣ Show difference between == and is
"""
num1 = 5
num2 = 5
print("by using num1 == num2", num1 == num2)
print("by using is operator", num1 is num2)
"""
7️⃣ Swap two numbers using assignment operators
"""
a, b = 2, 3
print("before swappig ", a, b)
b, a = a, b
print("after swappig ", a, b)
"""
8️⃣ Convert string input to int and float safely
"""
my_input_str = input("Enter a string to convert into int and float: ")
print("integer value, ", int(my_input_str))
print("float value, ", float(my_input_str))
"""
9️⃣ Demonstrate precedence of operators
""""""
🔟 Create a small calculator using operators only
"""

def add(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

