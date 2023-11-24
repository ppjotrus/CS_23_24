name = input("What is your name?: ")
name = name.title()
print("Hello",name)
age = int(input("How old are you?:"))

if age < 17:
    print(f"Dear",{name}," You are too young to apply for a driving licence")
else:
    print("Dear",name,". You can apply for a driving licence")