# Developed by Chris

# Question 1
print("1. What does this program print out? (Remember: TWO answers. Your guess and the actual result. Label both.)\n")
print("Guess:")
print("0\n2\n4\n6\n8\n10")

print("Actual Code")
x = 0
while x < 10:
    print(x)
    x = x + 2
print("\n")

# Question 2
print("2. What does this program print out?")
print("Guess:")
print("1\n2\n4\n8\n16\n32\n64")

print("Actual Code:")
x = 1
while x < 64:
    print(x)
    x = x * 2
print("\n")

# Question 3
print("3. Why is the ``and x >= 0'' not needed?")
print("it is not needed as it will stop executing as soon as the value is less than 10")
print("\n")

# Question 4
print("4. What does this program print out? (0 pts) Explain. (1 pt)")
print("Guess:")
print("The program will print a countdown  and once done it will return blast off")
print("\nActual Code:")
x = 5
while x >= 0:
    print(x)
    if x == "1":
        print("Blast off!")
    x = x - 1
print("\n")

# Question 5
print("5. Fix the following code so it doesn't repeat forever, and keeps asking the user until he or she enters a number greater than zero: (2 pts)")

# old code
''' 
x = float(input("Enter a number greater than zero: "))
 
while x <= 0:
    print("Too small. Enter a number greater than zero: ")
'''

# Fixed Code
x = 0
 
while x <= 0:
    x = float(input("Enter a number greater than zero: "))
    if x > 0:
        print("Great, the number is larger Than Zero!")
    if x < 1:
        print("Too small. Enter a number greater than zero: ")

# Question 6
print("6. Fix the following code:")

# Old Code
'''
x = 10
 
while x < 0:
    print(x)
    x - 1
 
print("Blast-off")
'''

# Fixed Code
x = 10
 
while x > 0:
    print(x)
    x = x - 1
    if x == 0:
        print("Blast-off")

print("\n")

# Question 7
print("7. What is wrong with this code? It runs but it has unnecessary code. Find all the unneeded code. Also, answer why it is not needed. (1 pt)")

# Old Code
'''
i = 0
for i in range(10):
    print(i)
    i += 1
'''

# Revised Code
for i in range(10):
    print(i)

print("\n")

# Question 8
print("8. Explain why the values printed for x are so different. (2 pts)")

# Code
'''
# Sample 1
x = 0
for i in range(10):
    x += 1
for j in range(10):
    x += 1
print(x)
 
# Sample 2
x = 0
for i in range(10):
    x += 1
    for j in range(10):
        x += 1
print(x)
'''

print("it outputs a different answer because the first example does not have loops nested into loops but the second one does.")