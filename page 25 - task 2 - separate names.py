#Page 25
#Task 2
#separate names

name = input("Please type your full name: ")
place = name.index(" ") # tell me where is "space"

fName = name[:place] #read the string until the "space"
sName = name[place+1:] #read the string after the "space"

print("First name is: "+fName+" and surname is "+sName)
