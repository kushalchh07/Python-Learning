def add(x, y):
    """
    Adds two numbers together and returns the result.

    Args:
        x (int or float): The first number to be added.
        y (int or float): The second number to be added.

    Returns:
        int or float: The sum of the two input numbers.
    """

    # Add the two input numbers and return the result
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first number and returns the result.

    Args:
        x (int or float): The first number to be subtracted from.
        y (int or float): The second number to be subtracted.

    Returns:
        int or float: The difference between the two input numbers.
    """
    # Subtract the second input number from the first one and return the result
    return x - y


def multiply(x, y):
    """
    Multiplies two numbers together and returns the result.

    Args:
        x (int or float): The first number to be multiplied.
        y (int or float): The second number to be multiplied.

    Returns:
        int or float: The product of the two input numbers.
    """
    # Multiply the two input numbers and return the result
    return x * y




def divide(x, y):
    """
    Divides the first number by the second number and returns the result.

    Args:
        x (int or float): The first number to be divided.
        y (int or float): The second number to divide by.

    Returns:
        int or float: The result of the division.
    """
    # Check for division by zero
    if y == 0:
        return "Error! Division by zero."
    else:
        # Divide the two numbers and return the result
        return x / y

def calculator():
    """
    This function allows the user to perform basic arithmetic operations like addition, subtraction, multiplication, and division.
    It prompts the user to select an operation and input two numbers to perform the operation on.
    The results are displayed to the user, and they can choose to perform another calculation or exit the calculator.
    """

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid input")

if __name__ == "__main__":
    calculator()
