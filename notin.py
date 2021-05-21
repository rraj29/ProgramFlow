activity = input("What would you like to do today? ")

if "cinema" not in activity:
    print("But,I  want to go to the cinema.")
##Note that:
# In python, the STRING COMPARISON IS CASE-SENSITIVE.
# So, if we write "I want to go to Cinema". then also it will print "But, I WANT TO....."
# So, to counter that: We'll use the CASEFOLD FUNCTION'

if "cinema" not in activity.casefold():
    print("But,I want to go to the CINEMA.")