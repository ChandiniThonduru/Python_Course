"""
Write a single Python script (day1_summary.py) that:

Takes user details (name, experience, skills list).

Stores them in a dictionary.

Checks the experience level (Junior/Mid/Senior).

Prints all details using string formatting.

💡 Bonus: Save the output into a text file.

"""
name = input("User Name: ")
exp = int(input("Experience: "))
skills = list(input("Skills aquired: ").split(" "))
dict1 = {
    "name": name,
    "exp": exp,
    "Skills": skills
}
if exp < 1:
    print("Junior")
elif 1 >= exp <= 2:
    print("mide level")
else:
    print("senior")

print(f"This is {name}, with {exp}+ experience in {skills}")
#using dictionary
print(f"This is {dict1["name"]}, with {dict1["exp"]}+ experience in {dict1["Skills"]}")

with open("demo_file.txt", "wt") as f:
    f.write(f"This is {name}, with {exp}+ experience in {skills}")
