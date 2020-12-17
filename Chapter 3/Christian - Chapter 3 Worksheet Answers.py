# Developed By Christian

# Question 1
print("Question 1")
print("use int not float")
def tempDemo():
    temperature = int(input("Temperature: "))
    if temperature >= 90:
        print("It is hot outside.")
    else:
        print("It is not hot out.")
print("\r")

# Question 2
print("Question 2")
print("run function q2 to run code")
def q2():
    usrIn = int(input("enter a positive or negative number"))
    if usrIn > 0:
        print("You entered the number", usrIn, "which is a postive number")
    if usrIn == 0:
        print("you entered the number", usrIn, "which is null")
    if usrIn < 0:
        print("you entered the number", usrIn, "which is a negative number")
print("\r")

# Question 3
print("Question 3")
print("run function q3 to run code")
def q3():
    usrIn = int(input("enter a number to see result"))
    if usrIn > -10 or usrIn < 10:
        print("sucess")
print("\r")

# Question 4
print("Question 4")
print("There is no variable to compare to")
def q4():
    user_input = input("A cherry is a: ")
    print("A. Dessert topping")
    print("B. Desert topping")
    if user_input.upper() == "A":
        print("Correct!")
    else:
        print("Incorrect.")
print("\r")

# Question 5
print("Question 5")
print("you can only have one \"==\" not two \"==\"")
print("The second issue is that there is no condition for handling negative number whcih will return an error")
def q5():
    x = int(input("type a number"))
    if x >= 0:
        print("x is positive.")
    if x < -1:
        print("x is negative")
    else:
        print("x is unknown")
print("\r")

# Question 6
print("Question 6")
print("the input field must be set to an \"int\" or \"float\"")
print("there is also a colon missing after the first if")
print("there is no condition for any number besides 6")
print("there nedds to be two \"==\" not one \"=\" for the if")
def q6():
    x = int(input("Enter a number: "))
    if x == 3:
        print("You entered 3")
    else:
        print("the  number is not 6")
print("\r")

# Questio 7
print("Question 7")
print("there is undefined var being used for the if statment instead of the vr \"answer\"")
print("else has no colon")
print("input data type is not specified")
print("there nedds to be two \"==\" not one \"=\" for the if")
def q7():
    answer = str(input("What is the name of Dr. Bunsen Honeydew's assistant? "))
    if answer == "Beaker":
        print("Correct!")
    else:
        print("Incorrect! It is Beaker.")
print("\r")

# Question 8
print("Question 8")
print("data type is not specified for input and there is alos no else")
def q8():
    x = tsr(input("How are you today?"))
    if x == "Happy" or "Glad":
        print("That is good to hear!")
print("\r")

# Question 9
print("Question 9")
print("I think \"X \" and \"Y\" will output fizz nad \"Z\" will output Buzz")
def q9():
    x = 5
    y = x == 6
    z = x == 5
    print("x=", x)
    print("y=", y)
    print("z=", z)
    if y:
        print("Fizz")
    if z:
        print("Buzz")
print("\r")

# Question 10
print("Question 10")
print("My Guess\nA) TRUE\nB) FALSE\nC) TRUE\nD) FALSE\nE) FALSE\nF) FALSE\nG) 5.00000000001\nH) TRUE\nI) FALSE\nJ) TRUE")
print("\r")
print("Actual")
x = 5
y = 10
z = 10
print(x < y)
print(y < z)
print(x == 5)
print(not x == 5)
print(x != 5)
print(not x != 5)
print(x == "5")
print(5 == x + 0.00000000001)
print(x == 5 and y == 10)
print(x == 5 and y == 5)
print(x == 5 or y == 5)
print("\r")

# Question 11
print("Question 11")
print("My Guess:\nA) TRUE\nB) FALSE\nC) TRUE\nE) FALSE\nF) FALSE\nG) TRUE\nH) FALSE")
print("\r")
print("Actual")
print("3" == "3")
print(" 3" == "3")
print(3 < 4)
print(3 < 10)
print("3" < "4")
print("3" < "10")
print( (2 == 2) == "True" )
print( (2 == 2) == True )
print("3 < \"3\" = syntx error")

# Question 12
print("Question 12")
print("needs to set input data type\nalso needs to check if STR is equal in Value and Type by putting two equals\"==\" not one\"=\" \nalso no such thig as \"else if\", you need either \"if\" or \"else\" in this case \"if\"\n\"user_input\" must be string inside \"if\"")
def q12():
    print("Welcome to Oregon Trail!")
 
    print("A. Banker")
    print("B. Carpenter")
    print("C. Farmer")
 
    user_input = str(input("What is your occupation? "))
 
    if user_input == "A":
        money = 100
    if user_input == "B":
        money = 70
    if user_input == "C":
        money = 50
 
    print("Great! you will start the game with", money, "dollars.")

# Done