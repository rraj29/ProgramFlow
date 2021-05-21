split_string = "This string has\nbeen split\nin many\ndifferent\nlines."
print(split_string)

tabbed_string= "1\t2\t3\t4\t5"
print(tabbed_string)

#use of single quotes and double quotes, how to print them
print('The pet shop owner said "No,no,\'e\'s uh,...he\'s resting".')
#note that for printing ' in the upper string we had to use \' because, the outermost was limited by single quotes.
print("The pet shop owner said \"No,no,'e's uh,...he's resting\".")
#here, similarly we had to use \" to print " because the delimiter is "".

#the best option: Use triple quotes to limit the string """kdj..djkk""", then we do not need to anything else
print("""The pet shop owner said "No,no,'e's uh,...he's resting".""")

#this method stops the use of delimiters in the strings
another_string = """This line has
been split 
over different
lines."""

print(another_string)

#the use of \ is to escape the delimiter. It escapes the delimiter, as we saw in the above examples.
yetAnotherSplitString = """This line has \
been split \
over different \
lines."""

print(yetAnotherSplitString)

#To print \ we can't simply do it. We have to do it by adding 2 \\ or declaring a 'row' string
#print("C:\Users\timbuchalka\notes.txt") ---- this won't work as expected due to \U, \t, \n being present.
#Use this method generally.
print("C:\\Users\\timbuchalka\\notes.txt")
#add 'r' at the starting to declare it as a row string, then it will print what's written. try to avoid this method
print(r"C:\Users\timbuchalka\notes.txt")