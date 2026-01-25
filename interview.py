from functools import reduce

add = lambda *args: sum(args)

print(add(2, 3))

print(add(2, 3, 8))


def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def add(a, b):
    return a + b

myList = [2, 5, 6, 4, 5, 9]
even_numbers = list(filter(even, myList))
even_numbers1 = list(filter(lambda n:n%2 == 0, myList))
square_numbers = list(map(lambda n:n*2, myList))
print(even_numbers1)
print(square_numbers)
reduced_list = reduce(add, square_numbers)
print(reduced_list)


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def PersonInfo(self):
        print("This is {} of {}".format(self.name, self.age))


class Student:
    def __init__(self, sid, fees):
        self.sid = sid
        self.fees = fees

    def StudentInfo(self):
        pass


class Teacher:
    def __init__(self, eid, sal):
        self.eid = eid
        self.sal = sal

    def TeacherInfo(self):
        pass


def mygen():
    for i in range(1, 20):
        if i % 2 == 0:
            yield i


mygen1 = mygen()
for i in mygen1:
    print(i)
