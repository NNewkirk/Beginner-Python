# This is my first python program I'm creating without a tutorial
# I've made a similar calculator in Java and C++

# I'm predefining these values so my while loop can continuously
cont, sum1 = 1, 1

while cont == 1:
    func = input("Hello, Welcome to Newkirk's simple calculator\n"
                 "Chose your function: addition,subtract,divide,multiply \n ")
# func will be used to decide which function the user wants to do

# These capture input a and b
    a = float(input('Input A: '))
    b = float(input('Input B: '))

# This Match-Case statement runs through whichever choice the user picks for their calculations
    match func:
        case "divide":
            sum1, cont = (a/b), 2
        case "addition":
            sum1, cont = (a+b), 2
        case "subtract":
            sum1, cont = (a-b), 2
        case "multiply":
            sum1, cont = (a*b), 2
        case _:
            func, cont = input("Please retype your function: "), 1

print("Here is your final answer", sum1)
