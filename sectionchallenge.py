options = int(input("Please choose one of the following options:\n1. Learn Python\n"
                "2. Learn swimming\n3. Go playing\n4. Go running\n0. exit"))
a = [1,2,3,4,0]
while options not in a:
    options = int(input("Please choose one of the following options:\n1. Learn Python\n"
                    "2. Learn swimming\n3. Go playing\n4. Go running\n0. exit"))
while options in a:
    print("Okay, you chose {}".format(options))
    options = int(input("Please choose one of the following options:\n1. Learn Python\n"
                        "2. Learn swimming\n3. Go playing\n4. Go running\n0. exit"))
    if options == 0:
        break

