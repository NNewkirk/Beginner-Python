# This is my first python program I'm creating without a tutorial
import matplotlib.pyplot as plt

# I'm predefining these values so my while loop can continuously
cont, sum1 = 1, 1
print("Hello, Welcome to Newkirk's simple calculator")

while cont == 1:
    func = input("Chose your function: addition,subtract,divide,multiply,graph \n ")
# func will be used to decide which function the user wants to do

# These capture input a and b
    if func != "graph":
        a = float(input('Input A: '))
        b = float(input('Input B: '))
    else:
        print("When inputting X and Y coordinates make sure to an equal quantity of both\n")
        x = list(input('Input your x coordinates: '))
        y = list(input('Input your y coordinates: '))

# This Match-Case statement runs through whichever choice the user picks for their calculations
    match func:
        case "divide":
            sum1 = (a/b)
        case "addition":
            sum1 = (a+b)
        case "subtract":
            sum1 = (a-b)
        case "multiply":
            sum1 = (a*b)
        case "graph":
            plt.plot(x, y)
            plt.show()
        case _:
            func, cont = input("Please retype your function: "), 1
# This prints the final value
    print("Here is your final answer", sum1)
# This prompts the user if they want to continue
    cont = int(input("Would you like to continue? Enter 1, if not enter 0. \n"))
