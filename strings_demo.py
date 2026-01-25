"""
Take input from the user (input()) for name and years of experience.

Print a formatted message: "Hi <name>, you have <years> years of experience!"

Try slicing and reversing your name using slicing [:: -1].
"""

name = input("Enter your Full Name :")
exp = input("Enter your Experience :")
print(f"Hi {name}, you have {exp} years of experience!")

first_name = name.split()[0]
last_name = name.split()[1]
print(first_name, last_name)
reverse_name = name[::-1]
print(reverse_name)
