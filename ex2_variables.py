# All programs can be thought of as mathematical operations on some data.

# In Python there are very few "raw" data types, the most common are:
#   Integers: whole numbers that have no decimal points.
#   Floating point numbers: real numbers that have decimal points.
#   Characters: a single character from the Unicode Alphabet.
#   Strings: Collections of characters

# Primitive Data Types
integers = 1
floating_points = 1.1
characters = 'h'
strings = "hello"


# You can do stuff with variables, like maths!

a = 1
b = 2

c = a + b
print(c)

d = a * b
print(d)

# These primitive data types can be combined into "lists", ordered sequences of data.

# Lists
# Can be made of anything
integer_lists = [1, 2, 3, 4, 5]
string_lists = ["hello", "there", "friend"]


# You can add to the end of a list with .append()
test_list = [1, 2, 3, 4, 5, 6]
test_list.append("Potato")
print(test_list)

# You can also combine lists using + 
added_lists = [1, 2, 3] + [4, 5, 6]
print(added_lists)

# You can get a specific element of a list with [n], called indexing
print(test_list[0])

# You can also index a list in reverse with negative numbers. E.g., [-1] will access the last element in a list.
print(test_list[-1])

# You can also get a series of values by using [start:stop]
# the following prints out the second value up to the second last
print(test_list[1:-2])