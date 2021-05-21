answer=5

print("Please guess a number between 1 to 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher.")
    guess = int(input())
    if guess == answer:
        print("Great, you got it.")
    else:

        print("Bad luck! Come again later..")
elif guess > answer:
    print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Great, you got it.")
    else:
        print("Bad luck! Come again later..")
else:
    print("Yayy, you got it right first time.")


# The IF will always be evaluated.
# We can have multiple ELIF blocks after that if we want.
# The ELIF statement has has to come after IF and before ELSE.
# So, the structure will be IF -> ELIF -> ELSE.
# ELSE MUST br at the LAST.
