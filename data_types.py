"""
Assignment 1:

Create 5 variables — your name, experience, current role, skills (list), and active status.

Print each with its type.

Modify your skills list by adding “Robot Framework” and “API Testing”.
"""
name = "Thonduru Chandini"  #str
experience = 3.5  #float
role = "Python Automation Engineer"  # string
skills = ["python", "pytest", "slash", "github", "selenium"]  #list
active_status = True  #bool

print(type(name))
print(type(experience))
print(type(role))
print(type(skills))
print(type(active_status))

skills.extend(["API Testing", "Robot Framework"])
print(skills)
