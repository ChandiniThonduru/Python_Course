#What is 7 to the power of 4
print(7 ** 4)

#str = 'Hi there Sam!' split into list
str1 = 'Hi there Sam!'
x = str1.split()
print(x)

#Use format
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet, diameter))

#Given this nested list, use indexing to grab the word "hello"
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
x = lst[3][1][2]
print(x)
#Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky
d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
x = d['k1'][3]
x1 = x['tricky'][3]
x2 = x1['target'][3]
print(x2)
#Differenve between list and tuple. tuples are immutable lists are mutable


# Create a function that grabs the email website domain from a string in the form:
# The key difference between tuples and lists is that while tuples are immutable objects, lists are mutable.
# Create a function that grabs the email website domain from a string in the form:
def domainGet(input):
    return input.split('@')[1]


print(domainGet("user@domain.com"))


# Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about
# edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def findDog(str):
    return "dog" in str.lower()


print(findDog("Is there a dog here"))


# Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.
def countOfDog(str):
    c = 0
    for i in str.lower().split():
        if i == "dog":
            c = c + 1
    return c


print(countOfDog("This dog runs faster than other dog dude!"))

#Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'

seq = ['soup','dog','salad','cat','great']
x = list(filter(lambda newseq:newseq[0] == 's', seq))
print(x)


# You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible
# results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If
# speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big
# Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your
# birthday, your speed can be 5 higher in all cases.


def caught_speeding(spd, brt):
    if brt:
        spd = spd - 5
    if spd <= 60:
        return 'No Ticket'
    elif (spd > 60) and (spd <= 80):
        return "Small Ticket"
    else:
        return "Big Ticket"


print(caught_speeding(81, True))
print(caught_speeding(81, False))

