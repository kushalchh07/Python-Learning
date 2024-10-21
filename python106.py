# Importing specific items

""" Python standard library
The Python Standard Library contains the exact syntax, semantics,
and tokens of Python. It contains built-in modules that provide access
    to basic system functionality like I/O and some other core modules.
    Most of the Python Libraries are written in the C programming language.
    The Python standard library consists of more than 200 core modules.
    All these work together to make Python a high-level programming language. 
    Python Standard Library plays a very important role. Without it,
    the programmers can’t have access to the functionalities of Python. 
    But other than this, there are several other libraries in Python that
    make a programmer’s life easier. Let’s have a look at some of the commonly used libraries:
"""    
   
from math import sqrt, sin # import only the sqrt and sin functions from the math module 
import datetime
A = 16
B = 3.14
print(sqrt(A))
print(sin(B))



# Getting the current date and time
current_time = datetime.datetime.now()
print(f"Current Date and Time: {current_time}")

# Formatting a date
formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# Creating a specific date
specific_date = datetime.datetime(2023, 12, 25)
print(f"Specific Date: {specific_date}")

