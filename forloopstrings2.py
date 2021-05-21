#   *We'll separate the delimiters/separators here from the number.
#This is a common phenomenon that occurs when we import the data from any other device.


number = input("Input a series of numbers with any separators that you want: ")     #asking the user to input a number.
#number = "1123.456;469/465.4826-6194$3654,66>369+54*115"                           #here, we had a number given
separators = ""
onlynumbers = ""

for char in number:
    if char.isnumeric():            #.isnumeric() is a string operation to check if a character is numeric or not.
        onlynumbers = onlynumbers + char
    else:
        separators = separators + char

print(onlynumbers)
print(separators)
