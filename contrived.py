numbers = [1,45, 32, 12, 60]

#ELSE in a LOOP.
#HERE, the use is different than that in IF statement.
#The ELSE STATEMENT will COME TO WORK ONLY IF THE WHOLE LOOP WORKS FULLY WITHOUT BREAKING ANYWHERE.

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The numbers are unacceptable.")
        break
else:
    print("The numbers are acceptable.")