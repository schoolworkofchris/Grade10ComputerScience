# Developed by Chris

import time
import random
import pygame
import pygame.mixer
pygame.mixer.init()
pygame.init()

# Main Vars
room_list = []
current_room = 0
done = False

# Room Data
roomDesc1 = "You are in the first bedroom, there are two halls, one to the east(2) and one to the south(4) "
room1 = [roomDesc1, None, 2, 4, None]
room_list.append(room1)

roomDesc2 = "you are in the north hall, you can go east into the kitchen (3), you can go south into the center of the dungeon(5), or you can go set into the first room (1)"
room2 = [roomDesc2, None, 3, 5, 1]
room_list.append(room2)

roomDesc3 = "You are in the kitchen, there is a hall to the west(2), there is also another hall to the south(6)"
room3 = [roomDesc3, None, None, 6, 2]
room_list.append(room3)

roomDesc4 = "you are in the west hall the is a room to the north(1), there is also another hallk to the east (5), and there is a second bedroom to the south(7)"
room4 = [roomDesc4, 1, 5, 7, None]
room_list.append(room4)

roomDesc5 = "You are in the center hall, there is a hall to the north(2), there is another hall to the east(6) there is an office to the south(8) and another hall to the west(4)"
room5 = [roomDesc5, 2, 5, 8, 4]
room_list.append(room5)

roomDesc6 = "You are in the east hall, there is a kithchen to the north(3), a living room to the south(6), and the center hall is the the west(5)"
room6 = [roomDesc6, 3, None, 9, 5]
room_list.append(room6)

roomDesc7 = "you are in the second bedroom, there is a hall to the north(4)"
room7 = [roomDesc7, 4, None, None, None]
room_list.append(room7)

roomDesc8 = "you are in the office, there is a hall to the north (5)"
room8 = [roomDesc8, 5, None, None, None]
room_list.append(room8)

roomDesc9 = "You are in the living room, there is a hall to the north (6)"
room9 = [roomDesc9, 6, None, None, None]
room_list.append(room9)

# Music Generator
musicS = random.randint(1, 3)

if musicS == 1:
    t1 = pygame.mixer.music.load("Chapter 7/Chapter 7 Lab/Clean_Break.mp3")
    t1 = pygame.mixer.music.play(0) 
if musicS == 2:
    t2 = pygame.mixer.music.load("Chapter 7/Chapter 7 Lab/Hanging_Out.mp3")
    t2 = pygame.mixer.music.play(0) 
if musicS == 3:
    t3 = pygame.mixer.music.load("Chapter 7/Chapter 7 Lab/Rest.mp3")
    t3 = pygame.mixer.music.play(0) 

# Main Loop
while done == False:
    print(room_list[current_room][0])
    choice = str(input("Choose a room: "))
    print("\n")

    if current_room == 0:
        if choice.lower() == "east" or choice == "2":
            current_room = 1
        if choice.lower() == "south" or choice == "4":
            current_room = 3

    if current_room == 1:
        if choice.lower() == "east" or choice == "3":
            current_room = 2
        if choice.lower() == "south" or choice == "5":
            current_room = 4
        if choice.lower() == "west" or choice == "1":
            current_room = 0

    if current_room == 2:
        if choice.lower() == "south" or choice == "6":
            current_room = 5
        if choice.lower() == "west" or choice == "2":
            current_room = 1

    if current_room == 3:
        if choice.lower() == "north" or choice == "1":
            current_room = 0
        if choice.lower() == "east" or choice == "5":
            current_room = 4
        if choice.lower() == "south" or choice == "7":
            current_room = 6

    if current_room == 4:
        if choice.lower() == "north" or choice == "2":
            current_room = 1
        if choice.lower() == "east" or choice == "6":
            current_room = 5
        if choice.lower() == "south" or choice == "8":
            current_room = 7
        if choice.lower() == "west" or choice == "4":
            current_room = 3
    
    if current_room == 5:
        if choice.lower() == "north" or choice == "3":
            current_room = 2
        if choice.lower() == "south" or choice == "9":
            current_room = 8
        if choice.lower() == "west" or choice == "5":
            current_room = 4

    if current_room == 6:
        if choice.lower() == "north" or choice == "4":
            current_room = 3

    if current_room == 7:
        if choice.lower() == "north" or choice == "5":
            current_room = 4

    if current_room == 8:
        if choice.lower() == "north" or choice == "6":
            current_room = 5
    
    if choice.lower() == "quit":
        done = True

    if choice.lower() == "none":
        print("Oops, looks like you cant go that way, try another room")