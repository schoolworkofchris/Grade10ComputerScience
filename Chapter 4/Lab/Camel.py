# Developed by Chris

# Libraries
import time
import random
import pygame
pygame.init()


# Vars
done = False
milesTraveled = 0
thirst = 0
tiredness = 0
distance_Natives = -20
canteenDrinks = 3
oasis = 0
oasisF = 7
validInput = ["a", "b", "c", "d", "e", "q"]
musicS = 0

# intro
print("Welcome to Camel!\nYou have stolen a camel to make your way across the great Mobi desert.\nThe natives want their camel back and are chasing you down! Survive your\ndesert trek and out run the natives.\n")    


# Random Music Selector
musicS = random.randint(1, 3)

if musicS == 1:
    t1 = pygame.mixer.music.load("Lab 4/Repeater.mp3")
    t1 = pygame.mixer.music.play(0) 
if musicS == 2:
    t2 = pygame.mixer.music.load("Lab 4/Scanner.mp3")
    t2 = pygame.mixer.music.play(0) 
if musicS == 3:
    t3 = pygame.mixer.music.load("Lab 4/I_Hear_Voices.mp3")
    t3 = pygame.mixer.music.play(0) 

# Main Loop
while done == False:

    # Options
    print("Select an option")
    print("A. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nF. Mute music\nQ. Quit.\n")

    # Get user input
    q1 = str(input("Enter your choice: "))

    # Validators
    if q1.lower() == "q":
        done = True
    if q1.lower() == "f":
        pygame.mixer.music.stop()
    if q1.lower() == "e":
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteenDrinks)
        print("The natives are", distance_Natives, "miles behind you.\n")
    if q1.lower() == "d":
        tiredness = 0
        print("Your cammel is happy")
        distance_Natives = distance_Natives + random.randint(7, 14)
        print(distance_Natives, "\n")
    if q1.lower() == "c":
        milesTraveled = milesTraveled + random.randint(10, 20)
        print("Miles traveled:", milesTraveled, "\n")
        thirst = thirst + 1
        tiredness = tiredness + random.randint(1, 3)
        distance_Natives = distance_Natives + random.randint(7, 14)
    if q1.lower() == "b":
        milesTraveled = milesTraveled + random.randint(5, 12)
        print("Miles travled", milesTraveled, "\n")
        thirst = thirst + 1
        tiredness = tiredness + 1
        distance_Natives = distance_Natives + random.randint(7, 14)
    if q1.lower() == "a":
        if canteenDrinks > 0:
            print("You drank from the canteen\n")
            canteenDrinks = canteenDrinks - 1
            thirst = 0
        else:
            print("You are out of drinks\n")

    # Oasis Calculator
    oasis = random.randint(1, 20)
    if oasis == oasisF:
        print("You found an oasis\n")
        canteen = 3
        thirst = 0
    if oasis < oasisF:
        oasis = random.randint(1, 20)
    
    # Vital Monitors
    if thirst > 4:
        if thirst > 6:
            print("You died of thirst\n")
            done = True
        else:
            print("You are thirsty\n")
    if tiredness > 5:
        if tiredness > 8:
            print("Your camel is dead\n")
            done = True
        else:
            print("Your camel is tired\n")
    if distance_Natives >= milesTraveled:
        print("The natives got you\n")
        done = True
    
    if milesTraveled >= 200:
        print("You have escaped\n")
        thirst = 0
        tiredness = 0
        end = pygame.mixer.music.load("/Users/chris/Google Drive/Grade 10 Computer Science/Python/Lab 4/Leveled_Up.mp3")
        end = pygame.mixer.music.play(0)
        time.sleep(1000)
        done = True