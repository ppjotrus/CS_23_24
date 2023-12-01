# Piotr Krupinski
# 01/12/2023
# simple while loop


def main(): #defining main function
    number = get_number()
    meow(number)
    

def get_number(): # defining functions which asks a user of how many mews they want
    while True:
        n = int(input("What is n?:"))
        if n > 0:
            break
    return n

def meow(n): # function printing meows as many times as the user declared
    for i in range(n):
        print("meow")
        

main() # starts the main function