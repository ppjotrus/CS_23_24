#01/12/23

# While loop with user input

def main(): #defining the function
    loops = ask_user()
    say_hello(loops)
    

def ask_user():
    n = int(input("How many loops?: "))
    return n

def say_hello(i):
    for j in range (i):
        print("Hello ")


main() # calling the function