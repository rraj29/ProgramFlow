age = int(input("How old are you ?"))

#if age>=16 and age<=65:
# if 16 <= age <= 65:               # this is the MOST EFFICIENT code for it.
if age in range(16,66):             #Using RANGE for this operation. NOT RECOMMENDED, just for checking
    print("Have a great day at work!")
else :
    print("Have a great day at your home...")

print("-"*80)

if age < 16 or age > 65:
    print("Have a great day at your home...")
else:
    print("Have a great day at work!")

## *** Using chained comparisons:
# While using AND CONDITION: Python will STOP as soon as it finds a FALSE STATAMENT
# While using OR CONDITION: Python will STOP as soon as it finds a TRUE STATAMENT