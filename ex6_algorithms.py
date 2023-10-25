# In this example we are going to do some basic statistical calculations 
# The main purpose is to get you thinking in Python, 
# i.e., how to use what you'v learned up until now.

###
# Problem 1. Write a function that calculates the mean of a list using no inbuilt functions.


# the mean can be calculated by finding the sum of all elements in a list
# then dividing the sum by the total number of elements
# i.e., mean = sum/total
def mean(xlist):
    # Create variables to hold our total and number of elements
    total = 0
    num_elem = 0
    # iterate through our list
    for i in xlist:
        # add the current element in the list to our running total
        total += i
        # add one to the number of elements we've seen so far
        num_elem += 1 

    # calculate the total divided by the number of elements (the mean), and return it
    return total / num_elem



test_list = [1, 2, 3, 4]
print(mean(test_list)) # should print out (1+2+3+4)/4 = 10/4 = 2.5


###
# Problem 2. Write a function that calculates the mean of a list using sum() and len()

def mean_2(xlist):
    return sum(xlist) / len(xlist)

print(mean_2(test_list)) # should print out (1+2+3+4)/4 = 10/4 = 2.5


### 
# Problem 3. use Numpy to calculate the mean much easier
# Numpy is a very standard Python package, that gives us a loooot of different cool mathematical and
# numeric functions, including a lot of basic statistic calculations.

# First step is to import Numpy, and give it a shorter name (np) so we can
# call on it faster and easier in our code
import numpy as np

print(np.mean(test_list))