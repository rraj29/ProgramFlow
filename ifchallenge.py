name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if 18<=age<31:
    print("Welcome to the holiday,{0}".format(name))
else:
    print("Sorry {0}, the slots are full.".format(name))