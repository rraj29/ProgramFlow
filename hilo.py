import random

low = 1
high = 1000

print("Please think of a number between {} and {}: ".format(low,high))
input("Press ENTER to start.")

guess = 1
cnt = 0
#while True:
while low!=high:
    print("\tSearching in the range of {} and {}.".format(low, high))
    guess = low + (high-low)//2
    cnt +=1
    high_low = input("My guess is {}. Should I guess higher or lower? "
    "Enter h or l, or c if my guess is correct".format(guess)).casefold()
    if high_low == "l":     #the guess was higher, and we want a lower value.
        high = guess - 1
    elif high_low =="h":        #the guess was lower, and we want a higher value.
        low = guess + 1
    elif high_low =="c":
        print("Yayy,I got it correct in {} guesses.".format(cnt))
        break
    else:
        print("Enter l, h or c.")

else:
    print("You guessed of the number {}.".format(low))
    print("I got it in {} guesses.".format(cnt))
    # this ELSE is also the LOOP one only. this is bullshit. DO NOT USE IT in your codes.
