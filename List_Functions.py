List = list([123, "String", 'C', "Chandini"])
print(List)

List[2] = "Hello"  #Changing Value in Index 2
print(List)

List[-2] = "World"  #Accessing from last
print(List)

print(List[::-1])  #Accesing List in reverse
print(List[2:4:1])  #Accesing List in range
print(List[2:0:-1])  #Accesing List in reverse range

# append() method
List.append(2001)
print(List)

# insert() method
List.insert(2, 100)
print(List)

# extend() method
List1 = list(["Python", "java", 1, 5.65])
List1.extend(List)  # List1 will change, List will be same
print(List)
print(List1)

#sum() method
List = [1, 2, 3, 4, 5]  #List is Updated
print(sum(List))

#print(sum(List1)) # Error

#count() method
List = [1, 2, 3, 1, 2, 7, 2, 3, 2, 1]
print(List.count(1))

#len() method
print(len(List))

#index() method
print(List.index(2))  # first occurrence of 2
print(List.index(2, 7))  # check 2,  after occurrence of 7

#min() method
numbers = [5, 2, 8, 1, 9]
print(min(numbers))

#max() method
print(max(numbers))

#sort() method
List = [1, 2, 7, 4, 5, 35, 25]
List.sort(reverse=False)  # default reverse=False
print(List)
List.sort(reverse=True)
print(List)

#reverse() method
List = [1, 2, 3, 4, 5]
List.reverse()
print(List)

#pop() method
List = [1, 2, 3, 4, 5]
print(List.pop())
print(List.pop(2))
print(List)

#del() method
List = [1, 2, 3, 4, 5]
del List[3]
print(List)

#remove() method
List = [1, 2, 3, 4, 5]
List.remove(3)
print(List)

