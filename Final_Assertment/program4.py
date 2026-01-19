class Person:
    count = 0

    def __init__(self, firstName, lastName):
        self.firstName = firstName  # instance attribute
        self.lastName = lastName
        Person.count = Person.count + 1

    def display(self):
        print("First Name:", self.firstName)
        print("Last_Name:", self.lastName)


x = Person("Thonduru", "Chandini")
y = Person("Thonduru", "Maimoon")
x.display()
y.display()
print("Total instance of Person is :", Person.count)
