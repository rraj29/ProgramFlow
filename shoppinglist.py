shopping_list = ["milk", "pazzta", "eggs","spam", "bread", "rice"]

for item in shopping_list:
    if item != "spam":
         print("Buy " + item)

print("-"*51)


#same code, just CONTINUE is used there.
# When CONTINUE is encountered, the code goes to the next iteration without going forward.

for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)