shopping_list = ["milk", "pazzta", "eggs","spam", "bread", "rice"]

item_to_find = "albatross"
#The next initialization is important if the item is not found in the list. Otherwise we'll get error.
found_at = None

#we are searching for something, we need to find the index at which it is located

#for index in range(6)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break


#Python has some inbuilt functions that make it a good language. An example of that shown below:
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {0}".format(found_at))
else:
    print("{0} not found".format(item_to_find))


#BREAK gets us out of the loop completely. and staright away moves to print statement.
#This saves a lot of time, suppose the list was 1000 variables long,
#then iterating over it even after we found the position would be useless.