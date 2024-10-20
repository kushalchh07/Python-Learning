# Python Indentation 
"""
    Indentation refers to the spaces at the beginning of code
    where python looks for statement and loops
    ( There should be at least one space at the beginning of line)
    for example 

"""
''' if 5 > 2:
    print("Five is greater than two!")
     # Above code will not produce any error
if 5 > 2:
print("Five is greater than two!")

# Here above code will produce error
'''

# Comments in Python
# Single Line Comments

# This is a single line comment

# Multi Line Comments   
"""
This is a multi line comment
written in
more than just one line
""" 
# Python Variables
"""
Variables do not need to be declared with any particular type, and can even change type after they have been set. 
"""
x=5 #int
y="Kushal"#string
print(x)
print(y)



# Casting = If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
"""
    A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.


    """
    
    # Assign Multiple values

"""
    Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#python datatypes
"""
    Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
    """
    # we can get the type of any variable using type() function\

x = 5
y = "John"
print(type(x))
print(type(y))
"""  Output:  
<class 'int'>
<class 'str'>
    """
    
    #Python Boolean
    
""" In python there is true and false as boolean value  """
#example
print(10 > 9)  # Output: True
print(10 == 9)  # Output: False
print(10 < 9)  # Output: False

''' Python divides the operators in the following groups:

Arithmetic operators(+,-,*,/,%,**,//)
Assignment operators(=,+=,-=,*=,/=,%=,**=,//=)
Comparison operators(==,!=,>,<,>=,<=)
Logical operators(and,or,not)
Identity operators(is,is not)
Membership operators(in,not in)
Bitwise operators(&,|,^,~,<<,>>)
'''