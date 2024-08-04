#String format() Method
# The format method formats the specified value and insert them inside the string's placeholder.
# The placeholder is defined using curley brackets: {}. 

# named indexes:-
text1 = "Welcome {fname} {lname}".format(fname = "Aakash", lname = "Rambhad")

print(text1)

# numbered indexes:-
text2 = "Welcome {0} {1}".format("Aakash", "Rambhad")

print(text2)

# Empty placeholders
text3 = "Welcome {} {}".format("Aakash", "Rambhad")

print(text3)