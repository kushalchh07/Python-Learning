# Control Structures in Python

""" Types of Control Structures
Control flow refers to the sequence a program will follow during its execution.

Conditions, loops, and calling functions significantly influence how a Python program is controlled.

There are three types of control structures in Python:

Sequential - The default working of a program
Selection - This structure is used for making decisions by checking conditions and branching
Repetition - This structure is used for looping, i.e., repeatedly executing a certain piece of a code block.

"""

# Python program to show how a sequential control structure works  
  
# We will initialize some variables  
# Then operations will be done  
# And, at last, results will be printed  
# Execution flow will be the same as the code is written, and there is no hidden flow  
a = 20  
b = 10  
c = a - b  
d = a + b  
e = a * b  
print("The result of the subtraction is: ", c)  
print("The result of the addition is: ", d)  
print("The result of the multiplication is: ", e) 

# Selection Control Structure

'''
Only if
if-else
The nested if
The complete if-elif-else 
''' 
# simple if
""" 
syntax : 

if condition:
    statements

else:
    statements
    
"""
#example
if(5<2):
    print("5 is less than 2")
else:
    print("5 is not less than 2")