parrot = "Norwegian Blue"

letter = input("Enter a character:")

if letter in parrot:
    print("{0} is in {1}.".format(letter,parrot))
else:
    print("I don't need the letter.")