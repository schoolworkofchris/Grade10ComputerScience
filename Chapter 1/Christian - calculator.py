# Developed By Christian Moloci
import math
import operator

# hi there Mrs. G, here is my calculator, as you can see it fairly complex, I was able to do this as I already had knoledge in other prgramming languages
# which allowed me to just seacrh up syntax for stuff such as if staements and functions which enabled me to create this fantastic mulit-purpose calculator
# I also added 2 extra calculators as a bonus

# sum calculator
def calculator1():
    ops = {
        #thanks to Matthew Flaschen and Eeshaan on stack overflow for helping me with converting strings into ops!!!py
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    print("welcome to the sum calculator")
    num1 = input("Enter first number ", )
    op = input("enter op ", )
    opSum = ops[op]
    num2 = input("enter second num ", )
    sum = num1 + op + num2
    print(eval(sum))
    print("\r")
    calcFind()

# standardarea converter
def calculator2():
    ops = {
        "*": operator.mul
    }
    per1 = input("please enter first number ")
    per2 = input("please enetr second number ")
    op1 = "*"
    finalOp = ops[op1]
    area = per1 + op1 + per2
    print(eval(area))
    print("\r")
    calcFind()
    
#average claculator
def calculator3():
    ops = {
        "+": operator.add,
        "/": operator.truediv
    }
    name = input("Name: ")
    print("Hello There", name)
    class1 = input("enter your first class ")
    class2 = input("enter your second class ")
    class3 = input("enter your third class ")
    class4 = input("enter your fourth class ")

    mClass1 = input("what mark did you get for " + class1 + " ")
    mClass2 = input("what mark did you get for " + class2 + " ")
    mClass3 = input("what mark did you get for " + class3 + " ")
    mClass4 = input("what mark did you get for " + class4 + " ")

    opAdd = "+"
    opDiv = "/"
    divider = 4
    opFinal1 = ops[opAdd]
    opFinal2 = ops[opDiv]
    averageCalc1 = mClass1 + opAdd + mClass2 + opAdd + mClass3 + opAdd + mClass4
    averageCalc1 = (eval(averageCalc1))
    averagecalc2 = averageCalc1 / divider
    finalAverage = averagecalc2
    if finalAverage >= 70:
        print("Great job, you got", finalAverage, "%")
    elif finalAverage < 70:
        print("hmm, looks like you could have done better, you got", finalAverage, "%")
    print("\r")
    calcFind()

#farenhight Calculator 
def calculator4():
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    } 
    opA = "+"
    opB = "/"
    opC = "*"
    opD = "-"
    finalOpA = ops[opA]
    finalOpD = ops[opB]
    finalOpC = ops[opC]
    finalOpD = ops[opD]

    print("Fahrenheit to Celcius Calculator")
    fahrenheit = input("enter Fahrenheit unit ")
    celcius = eval((fahrenheit + opD + "32"))
    celcius2 = celcius * 5 / 9
    print("in celcius, the temperature is", celcius2, "instead of", fahrenheit)
    print("\r")
    calcFind()

#Area of a trapazoid calculator
def calculator5():
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    } 
    print("welcome to area of a trapazoid calculator")
    opAdd = "+"
    opDivide = "/"
    opMultiply = "*"
    opSubtract = "-"
    finalOpAdd = ops[opAdd]
    finalOpDivide = ops[opDivide]
    finalOpMultiply = ops[opMultiply]
    finalOpSubtract = ops[opSubtract]
    base1 = input("base A ")
    base2 = input("base B ")
    height = input("height ")
    divider = "2"
    trapAreaStep1 = eval(base1 + opAdd + base2)
    trapAreaStep1 = str(trapAreaStep1)
    trapAreaStep2 = eval(trapAreaStep1 + opDivide + divider)
    trapAreaStep2 = str(trapAreaStep2)
    finalTrapArea = eval(trapAreaStep2 + opMultiply + height)
    print("Your Trapazoid Has an area of", finalTrapArea)
    print("\r")
    calcFind()


def calcFind():
    print("please type a number for a calculator")
    calcSelect = input("Sum Calculator(1) Area Calculator for rectangle/square(2) Average Calculator(3) Fahrenheit to Celcius(4) Trapazoid Calculator(5) Exit(exit)")
    print("\r")
    if calcSelect == "1":
        calculator1()
    if calcSelect == "2":
        calculator2()
    if calcSelect == "3":
        calculator3()
    if calcSelect == "4":
        calculator4()
    if calcSelect == "5":
        calculator5()
    if calcSelect == "exit":
        print("bye")
    else:
        print("sorry, Unknown command, please try again")
        calcFind()

calcFind()
