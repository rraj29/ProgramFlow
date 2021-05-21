#This is just a better version of the guessinggame code.
import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("'{}' is not a valid input.".format(temp))


lowest = 1
highest = 1000
answer = random.randint(lowest,highest)
print(answer)  # TODO: Delete after testing

print("Please input a number between {0} to {1}: ".format(lowest,highest))
guess=0     #we can put it to be any number that is not the answer.
cnt=0
while guess != answer:
    guess= get_integer(": ")
    cnt +=1
    if cnt >= 10:
        print("Sorry bro, bad luck")
        break
    if guess==0:
        break
    elif guess == answer:
        print("Yayy you got it right in {} times!".format(cnt))
        break
    elif guess > answer:
        print("Please guess lower: ")
    else:
        print("Please guess higher: ")

