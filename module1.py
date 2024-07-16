# Tested with https://www.programiz.com/python-programming/online-compiler/

    #To get familiar with Python programming and its related Integrated Development Environment (IDE), begin by writing a simple Python script with any desired functionality.
# Addition - given two inputs and then give the sum
try: 
    print("Give me two numbers to add")
    a = int(input("Type a number: "))
    b = int(input("Type another number: "))
    sum = a+b
    print("The sum is ", sum)
    
    # Subtraction - subtract a new number from the sum to give a difference 
    print("Give me a number to subtract from the number")
    c= int(input("Type a number: "))
    diff = sum-c
    print("The difference is ", diff)
    
    # Multiplication - give a number and multiply the differce to get a product 
    print("Give me a number to multiply the answer")
    d = int(input("Type a number: "))
    product = diff * d
    print("The product is ", product)
    
    # Division - given a new number and product, give the factor and remainder
    try:
        f = int(input("Type a number: "))
        factor = int(product / f)
        remainder = product % f
        print("the factor is", factor)
        print("R ", remainder )
    #Cant divide by zero! 
    except ZeroDivisionError as e:
        print(e)
except ValueError:
    print("Not a number.")

