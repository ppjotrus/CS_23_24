# Purpose: A program to demonstrate Boolean functions
# Purpose: A program to demonstrate Boolean functions

# A function to determine oddness
def isEven(number):
    if (number % 2 != 0):
        return True
    else:
        return False

# display even numbers < 100
for i in range (100):
     if isEven(i):           #boolean function receiving i and returning True or False
         print(i)

'''
# A function to determine evenness
def isEven(number):
    if (number % 2 == 0):
        return True
    else:
        return False

# display even numbers < 100
for i in range (100):
     if isEven(i):           #boolean function receiving i and returning True or False
         print(i)

'''