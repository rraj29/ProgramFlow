#    iterating over a RANGE in Python using FOR LOOP provides the same result as FOR LOOP in C.

for i in range(1,11):       #  it will print from 1 to 20 only.
    print("i is now {0}.".format(i))

#   default value for start is 0, and it is NOT NECESSARY to put a start value either.
for i in range(11):
    print("2 times {0} is {1}.".format(i,2*i))

#   we can also add STEP in for loop. BUT we need to put the starting point COMPULSORILY then.
for i in range(10,1,-2):
    print("{0} squared is {1}.".format(i,i**2))