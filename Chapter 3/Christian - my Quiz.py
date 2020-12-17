# Developed by Christian Moloci

# This test is going to be about building computers as I working on building one right now


#part 1
def partA():
    print("Welcome to the PC builders test.\nTake this test to find out how much you really know about building PC's")
    print("\r")
    print("Part A - Short Answers")

    global mark
    

    print("\r")
    a_Q1 = str(input("1) What does CPU stand for: "))
    if a_Q1.lower() == "central processing unit":
        print("Correct")
        mark = 0
        mark = mark + 1
    else:
        print("Incorrect")
        mark = 0
        mark = mark + 0

    print("\r")
    a_Q2 = str(input("2) What is the reccomended amount of RAM in 2020: "))
    if a_Q2.lower() == "16gb" or a_Q2.lower() == "16gb ram" or a_Q2.lower() == "16 gb of ram" or a_Q2.lower() == "16":
        print("Correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0
    
    print("\r")
    a_Q3 = str(input("3) What does ram stand for: "))
    if a_Q3.lower() == "random access memory":
        print("Correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0

    print("\r")
    a_Q4 = str(input("4) What is the fastest type of storage: "))
    if a_Q4.lower() == "m.2" or a_Q4.lower() == "m.2 nvme":
        print("Correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0

    print("\r")
    a_Q5 = str(input("5) What liquid is used to keep the CPU cool: "))
    if a_Q5.lower() == "thermal paste" or a_Q5.lower() == "thermal pad":
        print("Correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0
    

def partB():
    print("Part B - Multiple Chocie")
    global mark
    
    print("\r")
    print("1) What is the latest gen of RAM")
    print("A - DDR3\nB - DDR8\nC - DDRAM4\nD - DDR4")
    b_Q1 = str(input("Enter choice: "))
    if b_Q1.lower() == "d" or b_Q1.lower() == "ddr4":
        print("correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0
    
    print("\r")
    print("2) If a CPU has 4 cores how many thredas does it have")
    print("A - 1\nB - 10\nC - 8\nD - 0")
    b_Q2 = str(input("Enter choice: "))
    if b_Q2.lower() == "c" or b_Q2.lower() == "8":
        print("correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0

    print("\r")
    print("3) Can you use windows without buying a product key?")
    print("A - No, it's illegal\nB - yes, but you dont get all features")
    b_Q3 = str(input("Enter choice: "))
    if b_Q3.lower() == "b" or b_Q3.lower() == "yes" or b_Q3.lower() == "yes, but you dont get all features":
        print("correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0

    print("\r")
    print("4) What does overclocking mean")
    print("A - Setting the time to a the future\nB - giving the PC too much power\nC - unlocking the full power of your hardware instead of keeping the preset lower speeds\nD - Making the clock run faster than normal time")
    b_Q4 = str(input("Enter choice: "))
    if b_Q4.lower() == "c" or b_Q4.lower() == "unlocking the full power of your hardware instead of keeping the preset lower speeds":
        print("correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0

    print("\r")
    print("5) What is the reccomended amount of airflow fans? this does NOT include the CPU fan and PSU fan etc")
    print("A - 1\nB - 2\nC - 3\nD - 4")
    b_Q5 = str(input("Enter choice: "))
    if b_Q5.lower() == "c" or b_Q5.lower() == "3":
        print("correct")
        mark = mark + 1
    else:
        print("Incorrect")
        mark = mark + 0
    
    print("\r")
    percent = mark / 10
    percent = percent * 100
    print("You Scored", mark, "on the test!")
    print("Thats a", percent, "percent")
    print("Thank you for taking the PC builders Test")
    print("\r")


partA()
partB()
