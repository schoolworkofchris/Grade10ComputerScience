# Developed By Chris

#Question 1
print("1. Explain how the computer coordinate system differs from the standard Cartesian coordinate system. There are two main differences. List both.")
print("First, the X coordinates work the same but the Y coordinates are reversed. Second, it covers the lower right qudrant while the Caryesian coordinae system usually focuses usually on the upper right")
print("\n")

# Question 2
print("2. Before a Python Pygame program can use any functions like pygame.display.set_mode(), what two lines of code must occur first?")
print("You must first run \"import pygame\" and then run \"pygame.init()\"")
print("\n")

# Question 3
print("3. Explain how WHITE = (255, 255, 255) represents a color.")
print("Just like many programming lanuguages python uses RGB or HEX for its color system, in this question the code is in RGB as there are three sets of numbers,\nRED is first, GREED is second, BLUE is last, in this case the code stands for WHITE")
print("\n")

# Question 4
print("4. When do we use variable names for colors in all upper-case, and when do we use variable names for colors in all lower-case? (This applies to all variables, not just colors.)")
print("We do this when we want a constant which its value cant be changed")
print("\n")

# Question 5
print("5. What does the pygame.display.set_mode() function do?")
print("it opens a window")
print("\n")

# Question 6
print("6. What does this for event in pygame.event.get() loop do?")
print("it listens for a function (Key being pressed, loose the game, etc)")
print("\n")

# Question 7
print("7. What is pygame.time.Clock used for?")
print("Sets a var to run a clock speed to be used for the frame rate of the game at the end of the main loop")
print("\n")

# Question 8
print("8. For this line of code: (3 pts) \npygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5) \r- What does screen do? \n- What does [0, 0] do? \n- What does [100, 100] do? \n- What does 5 do?\n")
print("it displays a green line \n[0, 0] stands for the begining coordinates\n[100, 100] stands for the end coordinates\nthe 5 stands for the thickness of the line")
print("\n")

# Question 9
print("9. What is the best way to repeat something over and over in a drawing?")
print("the most efficient way is to create and offset var and add a ceratin distance until the var is equal to a certain number in a for loop")
print("\n")

# Question 10
print("10. When drawing a rectangle, what happens if the specified line width is zero?")
print("rather than the line being a certain number of pixels thick the rectangle will be fully filled with a color")
print("\n")

# Question 11
print("11. Describe the ellipse drawn in the code below.\nWhat is the x, y of the origin coordinate?\nWhat does the origin coordinate specify? The center of the circle?\nWhat is the length and the width of the ellipse? \rpygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)\r")
print("Y = 20, Y = 20\nit specifies the top left corner of the elipse which is invisible but is technically surrounded by a bounding box")
print("\n")

# Question 12
print("12. When drawing an arc, what additional information is needed over drawing an ellipse?")
print("The angle of the arc, typically is PI")
print("\n")

# Question 13
print("13. Describe, in general, what are the three steps needed when printing text to the screen using graphics?")
print("First, you must create a var with the meta (font style, font size, color, etc)\nnext you must create a variable to render the text, this is also where you specify the text you wish to output\nthen you must finnaly run the text\r")
print("\rExample:\nfont = pygame.font.SysFont('Calibri', 25, True, False) \ntext = font.render(\"My text\",True,BLACK) \nscreen.blit(text, [250, 250])")
print("\n")

# Question 14
print("14. When drawing text, the first line of the three lines needed to draw text should actually be outside the main program loop. It should only run once at the start of the program. Why is this? You may need to ask.")
print("This is because you are just creating a variable and you may want to use this variable more than once to display text with the same meta")
print("\n")

# Question 15
print("15. What are the coordinates of the polygon that the code below draws?\npygame.draw.polygon(screen, BLACK, [[50,100],[0,200],[200,200],[100,50]], 5)\n")
print("the top coordinates are X = 50 and Y = 100\nThe bottom left coordinates are X = 0 and Y = 200\nThe bottom right coordinates are X = 200 and Y = 200\nThe fourth adds a bump to the right side with X = 100 and Y = 50")
print("\n")

# Question 16
print("16. What does pygame.display.flip() do?")
print("It is required for anything to display in the window")
print("\n")

# Question 17
print("17. What does pygame.quit() do?")
print("Closes the window")
print("\n")

# Question 18
print("18. Look up on-line how the pygame.draw.circle works. Get it working and paste a working sample here. I only need the one line of code that draws the circle, but make sure it is working by trying it out in a full working program.")
print("Code: pygame.draw.circle(screen, GREEN, [300, 300], 50, 5)")
print("\n")