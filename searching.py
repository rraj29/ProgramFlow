shopping_list = ["milk", "pazzta", "eggs","spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

#we are searching for something, we need to find the index at which it is located
#we assume that it occurs at only one place.

#for index in range(6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
#BREAK gets us out of the loop completely. and staright away moves to print statement.
#This saves a lot of time, suppose the list was 1000 variables long,
#then iterating over it even after we found the position would be useless.

print("Item found at position {0}".format(found_at))