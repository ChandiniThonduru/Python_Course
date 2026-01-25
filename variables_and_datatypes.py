"""
Q1: Create variables for
your name
age
skills list
whether you are employed (True/False)
Print them in one line.
"""
name = "Chandini Thonduru"
age = 25
skills = ["Python", "Pytest", "slash", "Selenium", "Squish"]
employed = True
print("I am {} of age {} having experience in {}".format(name, age, skills))

"""
Q2: Convert int to float, float to string
"""
age = 25
print("type of age ", type(age))
float_age = float(age)
print("type of age", type(float_age))
print("type of age", str(float_age))

"""
Q3: Merge two strings using all 3 methods:
+ operator
f-string
format()"""
first_name = "Chandini"
last_name = "Thonduru"
print("using dot")
print(first_name + " " + last_name)
print("using f string")
print(f"my name is {first_name} {last_name}")
print("using format()")
print("my name is {} {}".format(first_name, last_name))
"""
Q4: Create a list with 5 different datatypes inside it.
"""
my_list1 = ["Chandini", "Thonduru", 25, True, 26.7, [1, 3, 4]]
print(my_list1)
"""
Q5: Write a program to find the datatype of user input.
"""
user_input = input("Enter any input to get the type of input you given")
print(type(user_input))  # this will always gives str only

"""
value = eval(user_input)
for this Use eval() to detect real datatype or 
 SAFE METHOD: Using ast.literal_eval()

Unlike eval(), this method cannot execute code.
It only converts valid Python literals, such as:
int,float,list,tuple,dict,set,boolean, None
So it is safe + clean + recommended for interviews.
"""

import ast

user_input = input("Enter anything: ")

try:
    value = ast.literal_eval(user_input)
    print("Detected type:", type(value))
except:
    print("Detected type: <class 'str'>")

"""
Q6: Check whether two variables are pointing to the same memory address.
"""
num1 = 5
num2 = num1
print("variables are pointing to the same memory address", id(num1) == id(num2), id(num1), id(num2))#True
print("variables are pointing to the same memory address", num1 is num2, id(num1), id(num2))#False