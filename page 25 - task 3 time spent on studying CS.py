#Page 25
#Task 3
#time spent on studying CS
print("Hello! How much time did you spend studying for CS exam?")

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))
print("The time you spent was",hours,":",minutes,":",seconds)
seconds_only = seconds + minutes*60 + hours*3600
print("Which is equivalent to:",seconds_only,"seconds")
              