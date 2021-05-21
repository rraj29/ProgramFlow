for i in range(1,13):
    for j in range(1,13):
        print("{0:2} times {1:<3} is {2:^4}.".format(i,j,i*j))
        #Recall:
        #{2:^4} -> 4 means that 4 spaces are allocated to i*j. and the numberwill try to be in the middle.
        #{1:<3} -> 3 means that 3 spaces are allocated to J. and the numberwill try to be in the left.
        #{0:<2} -> 2 means that 2 spaces are allocated to I. and the numberwill try to be in the right.
    print("-"*70)