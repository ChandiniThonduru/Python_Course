"""

Print all even numbers between 1–20 using both for and while loops.

Create a list of your tools and print only those containing the letter “t” or “T”.

Write a script that counts the number of vowels in your name.

"""

for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
#list compreshension
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even Numbers :",even_numbers)
tools = ["Pytest", "slash", "Robot"]

list1 = [x for x in tools if "t" in x]
print(list1)

name = "Thonduru Chandini"
c = 0
for i in name:
    if i in "aeiouAEIOU":
        c += 1
print(c)
