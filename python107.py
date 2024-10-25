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

#update tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#delete tuples  
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

 
