# Developed by chris
import random
import math

name = "Christian"
nameCount = 0

# Question 1
for namecCount in range(10):
    nameCount + 1
    print(name)
print("\n")

# Question 2
red = "red"
gold = "gold"
colorCount = 0

for colorCount in range(20):
    print(red)
    print(gold)
print("\n")

# Question 3
oddVar = 0
while oddVar < 100:
    oddVar = oddVar + 2
    print(oddVar)
print("\n")

# Question 4
numDwn = 11
while numDwn > 0:
    numDwn = numDwn - 1
    print(numDwn)
    if numDwn < 1:
        print("Blast Off")
print("\n")

# Question 5

#old
'''print("This program takes three numbers and returns the sum.")
total = 0
 
for i in range(3):
    x = input("Enter a number: ")
    total = total + i
print("The total is:", x)'''

# fixed
print("This program takes three numbers and returns the sum.")
total = 0
 
for x in range(3):
    x = int(input("Enter a number: "))
    total = total + x
print("The total is:", total)
print("\n")
print("first off i didnt exist so that had to be changed, i is replced by x\nnext off x in final print statment needed to be changed to total\nlast, input data type was not specified")
print("\n")

# Question 6
a = 0
while a < 10:
    a = a + 1
    print(a)
print("\n")

# Question 7
print(random.triangular(1, 10))
print("\n")

# Question 8
nums = 0
numTimer = 0
newNum = 0

def numCount():
    global numTimer
    numTimer = numTimer + 1
    

while numTimer < 7:
    nums = int(input("please enter a number: "))
    newNum = newNum + nums
    nums = 0
    numCount()
    if numTimer == 7:
        print("The Sum is:", newNum)
print("\n")

#Question 9
heads = 0
tails = 0
headsT = 0
tailsT = 0
coinT = 0
cSide = 0

while coinT < 50:
    cSide = random.randint(0, 1)
    coinT = coinT + 1
    if cSide == 1:
        heads = heads + 1
    elif cSide == 0:
        tails = tails + 1
print("Times on tails", tails,"Times on heads", heads)

# Question 10
defense = str(input("Rock(1) paper(2) scissors(3)"))
weapon = ["rock", "paper", "scissors"]
weaponSelect = random.choice(weapon)
print(weaponSelect)
if defense.lower() == "rock" or defense == "1":
    if weaponSelect == "rock":
        print("Tie")
    elif weaponSelect == "paper":
        print("you loose")
    elif weaponSelect == "scissors":
        print("Your Win")

if defense.lower() == "paper" or defense == "2":
    if weaponSelect == "rock":
        print("You Win")
    elif weaponSelect == "paper":
        print("Tie")
    elif weaponSelect == "scissors":
        print("You Loose")

if defense.lower() == "scissors" or defense == "3":
    if weaponSelect == "rock":
        print("You loose")
    elif weaponSelect == "paper":
        print("you Win")
    elif weaponSelect == "scissors":
        print("Tie")