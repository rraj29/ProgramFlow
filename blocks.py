name = input("Please enter your name: ")
age = input("How old are you, {0}? ".format(name))
print(age)
#Try doing the following:
#       print(age + 4)
#This won't occur. The problem will be coz INPUT FUNCTION RETURNS "STRING"


#So. in order to do that, we'll have to format it into an integer. That will be done as follows:
my_name = input("Who are you, buddy :")
#we'll have to TYPECAST it in the INTEGER format, to get any integer operation to work on it.
my_dob = int(input("Wanna know your age,{0} buddy... Please tell your birth year: ".format(my_name)))
print(2021-my_dob)

if 2021-my_dob < 18:
    print("Please come back in {} years.".format(18-2021+my_dob))
elif 2021-my_dob == 733:
    print("Hello Turtle!")
else:
    print("You are old enough to vote")
#the following code will also NOT work, because the ""age"" is a STRING, not an INTEGER. while "my_age" is an INT, so works.
#               if age > 18:
#                   print("Lele")
