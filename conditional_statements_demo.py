"""
Assignment 4:

Write a program that:

Takes your years of experience as input.

Prints:
"Fresher" if exp < 1
"Junior" if 1–2
"Mid-Level" if 3–4
"Senior" if ≥5
"""

exp = int(input("Experience: "))
if exp < 1:
    print("Fresher")
elif 1 >= exp <= 2:
    print("Junior")
elif 3 >= exp <= 4:
    print("Mide level")
else:
    print("Senior")
