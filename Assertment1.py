# count total number of digits in a number
n = int(input("Enter a number:"))
count = 0
while n != 0:
    n //= 10
    count += 1
print("Number of digits : % d" % count)

# print list of elements in reverse order using a loop
list1 = [1, 2, 3, 4, 5]
j = 0
rlist = []
print("Original list: ")
print(list1)
print("list in reverse order: ")
for i in range(len(list1) - 1, -1, -1):
    rlist.append(list1[i])
print(rlist)

# Display numbers from -20 to -5 using for loop
for i in range(-20, -4):
    print(i)


# Find the factorial of a given number

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter a number:"))
factorial = fact(num)
print("Factorial of %d = %d" % (num, factorial))

# Find the sum of the series upto n terms

term = int(input("Enter the term:"))
final_sum = 0
for n in range(1, term+1):
    final_sum = final_sum + n
print("Sum of 1st %d terms = %d" %(term, final_sum))


# Write a program to return multiple values from a function

def studentData():
    name = "Chandini"
    age = 22
    marks = [50, 60, 70, 80, 90]
    return name, age, marks


_name, _age, _marks = studentData()
print(f"name: {_name} \nage = {_age} \nmarks = {_marks}")


# Using function find the largest item from a given list

def findLargest(mylist):
    return max(mylist)


list1 = [1, 5, 7, 4, 0, 4, 8, 5, 7]
print("List is:", list1)
print("Largest element is:", findLargest(list1))

# Write a program to check if a value exists in a dictionary
dict1 = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight",
         "9": "Nine", "10": "Ten"}
values = dict1.values()
val = input("Enter the Value you want to Find: ")
if val in values:
    print(f"value {val} found in dictionary")
else:
    print(f"value {val} NOT found in dictionary")

# Write a program to Unpack the tuple ,list  into 4 variables
#tuple
a = (4, 8, 3, 9)
print(a)
n1, n2, n3, n4 = a
#unpack a tuple in variables
print(n1);print(n2);print(n3);print(n4)

# list
list1 = ["one", "Two", "Three", "Four"]
print(list1)
n1, n2, n3, n4 = list1
# unpack a list in variables
print(n1)
print(n2)
print(n3)
print(n4)

# Remove special charactors from a string
str = str(input('Enter a String:'))
b = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '*']
for i in b:
    str = str.replace(i, '')
print(str)
