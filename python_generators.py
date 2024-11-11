# Generators in Python What Are Generators?
#In Python, a generator is a type of iterator that is defined like a regular
# function but uses the yield keyword instead of return to produce a series of
# values. Each time the generator’s yield is executed, it "pauses" and saves its state.
# When you call the generator again, it resumes from where it left off.
def simple_generator():
    """
    A simple generator that yields the numbers 1, 2, and 3 in that order.

    Yields:
        int: The next number in the sequence (1, 2, 3).

    Examples:
        >>> for i in simple_generator():
        ...     print(i)
        1
        2
        3
    """
    
    
    yield 1
    yield 2
    yield 3

for i in simple_generator():
    print(i)
        
        
        #Fibonacci Numbers
def fibonacci():
    a, b = 0, 1
    while True:  # Infinite loop for infinite sequence
        yield a
        a, b = b, a + b

# Use the generator
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ") 
    
    #Summary of Key Points
    '''
    yield creates a generator function that returns an iterator.
next() can be used to fetch the next item from the generator.
Generators are memory-efficient and support lazy evaluation.
They are ideal for working with large data streams or infinite sequences.
    '''

            