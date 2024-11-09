#DATA STRUCTURES IN PYTHON

# Lists in python
"""
names =["Kushal","Rohit","Ram","Shyam"]
print(names) 
print(names[0])
print(names[1])
print(names[2])
print(names[3])

names.append("Sita") # adds sita to the end of the list
print(names)

names.remove("Ram") #removes ram from the list
print(names)

names.pop() #removes the last element
print(names)

names.sort() #sorts the list
print(names)

names.reverse() #reverses the list
print(names)

names.insert(2,"Gita") #inserts gita at index 2
print(names)



names[1]="pranita"
print(names) #replaces kushal with pranita


names.clear() #clears the list
print(names)
"""
#Tuples
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 
  """

"""
#update tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#delete tuples  
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)

 # remove item from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#unpacking tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

"""
"""
# using asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""
#loop through tuples
"""

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
  """
  
  #join tuples
"""
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
 """
#multiplying tuples
"""
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
 """
 #tuple methods
"""
#count method
fruits = ("apple", "banana", "cherry")
count = fruits.count("cherry")
print(count)
 
#index method
index = fruits.index("cherry")
print(index)
"""
"""
#sets in python
mySet = {"apple", "banana", "cherry"}
print(mySet)
#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
"""
"""
#acces set items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
"""
"""
#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# add a set to another set

#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#Add Any Iterable
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
#example

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
"""
#Remove "banana" by using the discard() method:
"""
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
"""
""" 
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""
"""
#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


#Use & to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.intersection_update(set2)

print(set1)
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"a", "b", "c"}  
set2 = {1, 2, 3}

set3 = set1.difference(set2)
print(set3)

#You can use the - operator instead of the difference() method, and you will get the same result.

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.difference_update(set2)

print(set1)
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, "c"}

set3 = set1.symmetric_difference(set2)
print(set3)

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set1 = {"a", "b", "c"}
set2 = {1, 2, "c"}

set1.symmetric_difference_update(set2)

print(set1)

"""
"""
  add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
  """
  #dictionaries in python
"""
Dictionary
Dictionaries are used to store data values in key:value pairs.


  A dictionary is a collection which is unordered, changeable and indexed and do not allow duplicates. In Python dictionaries are written with curly brackets, and have keys and values.
  """
"""
  #Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"]) # print the value of key brand
#dictionaries doesnot allow duplicate it overwrites the existing value of the key . 
thisdict1={
   "year":2020,
   "year":2021
 } 
print(thisdict1)# output will be {'year': '2021'}


# Function len() can be used to determine the length of the dictionary:
print(len(thisdict))
print(len(thisdict1))
"""
"""
# Dictionary can have values of different data types:
thisdict = {
  "brand": "Ford",#String
  "model": "Mustang",#string
  "year": 1964,#int
  "year": 2020,
  "madethisyear":False,#boolean
  "color":["red","blue"]#list
}
print(thisdict)
print(thisdict["color"]) # Output: ['red', 'blue']
print(thisdict["color"][1]) # Output: blue
# Function type() can be used to determine the type of a variable:
print(type(thisdict["color"]))

# the dict constructor can be used to make a dictionary:
thisdict = dict(name="John", age=36)
print(thisdict)
"""

# accessing the dictionary
# get() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

# keys() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)

# values() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)

# items() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)
# the pop() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# the popitem() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# the update() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
# the clear() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#change items in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2020
print(thisdict) 

# adding items in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)