class ListofStrings(list):
    def append(self, item):
        if not isinstance(item, str):
            raise TypeError("Only string objects can be added to the list.")
        if not item.istitle():
            item = item.title()
        super().append(item)


# Example usage:
string_list = ListofStrings()

try:
    string_list.append("PHP")
    string_list.append("SQL")
    string_list.append("Python")
    string_list.append(123)
except TypeError as e:
    print(e)

print(string_list)
