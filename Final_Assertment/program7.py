class MyNumbers:
    def __iter__(self):
        self.num = 19
        return self

    def __next__(self):
        if self.num >= 0:
            x = self.num
            self.num -= 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for i in myiter:
    print(i)
