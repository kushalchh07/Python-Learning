#DATA STRUCTURES IN PYTHON

# Lists in python
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