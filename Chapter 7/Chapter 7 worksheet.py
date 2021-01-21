# Developed by Chris

# 1. List the four types of data we've covered, and give an example of each:
a = 1
b = "a"
c = True
d = 1.3

print("Question 1")
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("\n")

# 2. What does this code print out? For this and the following problems, make sure you understand WHY 
# it prints what it does. You don't have to explain it, but if you don't understand why, make sure to ask.
# Otherwise you are wasting your time doing these.
print("The code is going to print the item based on the indexed number as seen here: ")
my_list = [5, 2, 6, 8, 101]
print(my_list[1])
print(my_list[4])
#print(my_list[5])
print("the last statment will return and error as 5 doesnt exist becaus most coding languages count 0 as a number (check source code)")

print("\n")

# 3. What does this code print out?
print("it will print all the items in the list on a new line")
my_list=[5, 2, 6, 8, 101]
for my_item in my_list:
    print(my_item)

print("\n")

#4. What does this code print out?
print("my_list2 will give an error as it is not a list (look in source code)")
my_list1 = [5, 2, 6, 8, 101]
# my_list2 = (5, 2, 6, 8, 101)
my_list1[3] = 10
print(my_list1)
# my_list2[2] = 10
#print(my_list2)

print("\n")

# 5. What does this code print out?
print("It will print 15 the first time because there is only one value because it is not comma seperated and then it is multiplied, the second time, you are rewriting the list so the only value is three and then it is printing the list 5 times")
my_list = [3 * 5]
print(my_list)
my_list = [3] * 5
print(my_list)

print("\n")

# 6. What does this code print out?
print("it will print 5 as thats the first value then it will add the value of i to the list everytime i changes untill the loop stops whcih then it will print the entire list")
my_list = [5]
for i in range(5):
    my_list.append(i)
print(my_list)

print("\n")

# 7. What does this code print out?
print("the first and second will print the length of the entire string, the thirf will meausre the length of the two strings then add those two numbers togethr, the third will also print the number of the string and the last one will give an error (Check Sourse Code)")
print(len("Hi"))
print(len("Hi there."))
print(len("Hi") + len("there."))
print(len("2"))
# print(len(2))

print("\n")

# 8. What does this code print out?
print("the first one will concatenated the second one will fully print out the first dtring but the second string will be parsed to just print the second letter of the word, the last one will just print the second letter of the first word as the [1] is outside the brackets instead of instead.")
print("Simpson" + "College")
print("Simpson" + "College"[1])
print( ("Simpson" + "College")[1] )

print("\n")

# 9. What does this code print out?
print("it will assign a new letter from word to letter everytime the loop is executed")
word = "Simpson"
for letter in word:
    print(letter)

print("\n")

# 10. What does this code print out?
print("it will concatenate college to word three times then print it")
word = "Simpson"
for i in range(3):
    word += "College"
print(word)

print("\n")

# 11. What does this code print out?
print("it will print word three times")
word = "Hi" * 3
print(word)

print("\n")

# 12. What does this code print out?
print("the first statment will print the third letter of my_text and the second one will print the second last letter of my_text")
my_text = "The quick brown fox jumped over the lazy dogs."
print("The 3rd spot is: " + my_text[3])
print("The -1 spot is: " + my_text[-1])

print("\n")

# 13. What does this code print out?
print("the first statment will print the first element of the string, the second one will print everything before the fourth element of s and teh last one will print all the elements after the second element")
s = "0123456789"
print(s[1])
print(s[:3])
print(s[3:])

# 14. Write a loop that will take in a list of five numbers from the user, adding each to an array. Then print the array. Try doing this without looking at the book.
usr_In = 0
my_list = []
cntr = 0

for cntr in range(5):
    usr_In = input("Enter an int number: ")
    usr_In = int(usr_In)
    my_list.append(usr_In)
print(my_list)

print("\n")

avgfnd = 0
avg_nums = 0
usr_nums = 0
nums_list = []
ii = 0
total_avg = 0

avgfnd = int(input("How many numbers would you like to calculate"))

for ii in range(avgfnd):
    usr_nums = input("enter and int: ")
    usr_nums = int(usr_nums)
    avg_nums = avg_nums + usr_nums
total_avg = avg_nums / avgfnd
print("The avarage of you ints is: ", total_avg)    