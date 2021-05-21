day= "Monday"
temperature = 30
raining = True

if day =="Saturday" and temperature > 27 and not raining:
    print("Go swimming.")
else:
    print("Learn Python.")

# truthy values
#        some things are treated as FALSE by default like 0,"",False,None.
# For example:
if 0:
    print("Hello")
else:
    print("See, I told you. 0 is evaluated as false always.")