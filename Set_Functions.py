myset = {"apple", "banana", "cherry"}
print(myset)

#add
myset.add("orange")
print(myset)

#update
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#remove
thisset.remove("banana")
print(thisset)

#discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#pop
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#clear
thisset.clear()
print(thisset)

#del
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) this gives error, because set already deleted

#union
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#symmetric_difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)