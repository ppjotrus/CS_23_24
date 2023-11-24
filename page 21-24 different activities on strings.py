# string.capitalize()
# string.upper()
# string.lower()
# value = len(string)
# string.__contains__()
#string.index()

mystring = "i Am in computer SCIENCE"
print(mystring.__contains__(" ")) #this checks if there
                                 #is a space " " in the string
#gives only TRUE or FALSE answer

place1 = mystring.index("m") # tell me where is letter m
print(place1)

place2 = mystring.index("comp") #tell me where does the substring comp start
print(place2)

print(mystring.capitalize())
print(mystring.upper())
print(mystring.lower())
myvalue = len(mystring)
#print(myvalue)
print(mystring[-3]) # 3rd from right
print(mystring[8:12]) # between 8 and 12
print(mystring[3:]) #start from 3 and continue to the end
print(mystring[:6]) # until 6th



