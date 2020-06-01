
while True:
    import math
    import math
    # Still underdevelopment...More updates to come...#
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract'to subtract two numbers")
    print("Enter 'multiply'to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'square' to find the square of a number")
    print("Enter 'cube' to find the cube of a number")
    print("Enter 'sqrt' to find the square root of a number")
    print("Enter 'cuberoot' to find the cube root of a number")
    print("Enter 'exp' to find the power of any number ")
    print("Enter 'circle' to find the area of a circle")
    print("Enter 'quit' to end the Program")
    print("Enter 'sin' to find the Sine value of a number")
    print("Enter 'cos' to find the cos value of a number")
    print("Enter 'tan' to find the tan value of a number")
    print("Enter 'quit' to close the console")
    user_input = input(": ")

    if user_input == "quit":
        print("THANKS FOR USING THIS CODE")
        break
    elif user_input == "add":
        num1 = float(input("Enter a Number: "))
        num2 = float(input("Enter a Number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "subtract":
        num1 = float(input("Enter a Number: "))
        num2 = float(input("Enter a Number:"))
        result = str(num1 - num2)
        print("The answer is " + result)
    elif user_input == "multiply":
        num1 = float(input("Enter a Number: "))
        num2 = float(input("Enter a Number: "))
        result = str(num1 * num2)
        print("The answer is " + result)
    elif user_input == "divide":
        num1 = float(input("Enter a Number: "))
        num2 = float(input("Enter a Number: "))
        result = str(num1/num2)
        print("The answer is " + result)
    elif user_input == "square":
        num1 = float(input("Enter a Number:"))
        result = str(num1*num1)
        print("The answer is " + result)
    elif user_input == "cube":
        num1 = float(input("Enter a Number:"))
        result = str(num1*num1*num1)
        print("The answer is " + result)
    elif user_input == "sqrt":
        num1 = float(input("Enter a Number:"))
        print(math.sqrt(num1))
    elif user_input == "cuberoot":
        num1 = float(input("Enter a Number:"))
        print(num1 ** (1./3))
    elif user_input == "exp":
        num1 = float(input("Enter a Number:"))
        num2 = float(input("Enter the power to be raised:"))
        print(num1 ** num2)
    elif user_input == "circle":
        r = float(input("Enter the radius of the Circle:"))
        π = 3.142
        print(  π * r * r )
    elif user_input == "sin":
        num1 = float(input("Enter a Number:"))
        sin_num1 = math.sin(math.radians(num1))
        print(sin_num1)
    elif user_input == "sin":
        num1 = float(input("Enter a Number:"))
        sin_num1 = math.sin(math.radians(num1))
        print(sin_num1)
    elif user_input == "cos":
        num1 = float(input("Enter a Number:"))
        cos_num1 = math.cos(math.radians(num1))
        print(cos_num1)
    elif user_input == "tan":
        num1 = float(input("Enter a Number:"))
        tan_num1 = math.tan(math.radians(num1))
        print(tan_num1)

    else:
        print("Unknown Input")

