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
        factor = product / f
        remainder = product % f
        print("the factor is", factor)
        print("R ", remainder )
    #Cant divide by zero! 
    except ZeroDivisionError as e:
        print(e)
except ValueError:
    print("Not a number.")

#Next, answer the following questions. Write out both the question and your answer:

#Why does it take so long to get software finished?
# Requirements are always changing and there are always unexpected problems, especially
# when dealing with new problems that arise when you try to adapt different technology to each other.

#Why are development costs so high?
# Costs are high namely because the requirements regarding labor and capitol expenses. Beyond that, there  are always delays that increase the overall cost of labor as well as things that need to be redone.

#Why can't we find all errors before we give the software to our customers?
# Given that we can't test for every contingency and use of the software the same way users might use it, and that there is a finite time and resource window to do testing, there has to be some sort of decision made in order to determine what level of faultiness is acceptable. For example, is it worth going aftere a problem that has a .01% chance of happening but will cost $100,000,000 if it happens or a problem that has a 1% chance of happening but will cost $1,000,000 if it happens? 

#Why do we spend so much time and effort maintaining existing programs?
# The costs of redisgning systems that already handle a lot of functionality are prohibitive and 
# the there could be additional costs incurred by by transitioning from a legacy to modern system. On top of this, there would be changing maintainence and infrastructure requirements. For example, going from onprem monoliths to cloud-based distributed systems would require an entire redoing of how the business operates. 

#Why do we continue to have difficulty in measuring progress, as software is being developed and maintained?
# A lot of progress can be difficult to quantify and sometimes, especially with differences in skill are involved, a situation can easily be imagined that the labor intensity or importance of a certain part of a project would not directly translate into how long something takes. Therefore %50 complete might really be more like 15% complete in many circumstances.
