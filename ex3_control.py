# Control Flow:
# is what we call controlling the flow of your code, 
# which means what parts of the code are run and how many times it runs.

# The most common form of control flow are "if statements"
# These statements check some condition, if a condition is true, one block of code is run
# if it is false another block of code is run instead
number = 10

print(f"Checking if {number} is greater than {5}")
if number > 5:
    print("Number is greater than 5")
else:
    print("Number is less than or equal to 5")


# The other type of control flow are repeated blocks of code, which is done using "loops".
# Loops are blocks of code that repeat a specified number of times, or until specified condition is met.


# FOR loops: repeats a certain number of times.

# Loops typically use some iteration variable, i, to track how many repetitions have been done.
# "range(n)" is a function that lists numbers from 0 to n, not inclusive of n.
# The line inside the loop will then repeat 10 times, from 0 up to and including 9. 

# in this case the iterator variable, i, will become the values 0..9 in order.
for i in range(10):
    print(i, end=', ')
print()

# WHILE loops: repeats until a condition is met
# Must ensure that the condition is eventually met, or you will loop forever!
i = 0
while i < 10:
    print(i, end=', ')
    # add 1 to i
    i += 1
print()

# Iterator loops: Loops through sequences such as lists
integer_lists = [1, 2, 3, 4, 5]
for i in integer_lists:
    print(i, end=', ')
print()
