# Probably the most important thing to learn for a statistician is how to work with external datasets.
# For this we're going to focus on CSV files. Usually associated with Excel, but they are just a 
# standard file format for storing text based data.

# CSVs are a Comma Separated Value files, which is made of a set of rows (line by line) with columns
# that are separated by commas.

# The first line on most CSV files is a header file, which gives the headings for each column.
# An example CSV is included in this project: "ex8.csv"

###
# Problem 1. Read CSV File Manually into a matrix

# You can use open(<path to file>) to open a file and read it as written.
test_file = open("ex8.csv")

# We will need a matrix where we can store our data.
data = []
# We also want a list of our headers (column names), so that we know what
# data we are using later on.
header = None
# The file can be read line by line by iterating through it like a list.
for line in test_file:
    print(line)
    # NOTE: the final element will have a '\n', this is a new line character
    # we can use the following line to select the whole line, except
    # for the final character, essentially cutting the new line character off.
    line = line[:-1]

    # The line can then be broken up into values by splitting it by ','s
    values = line.split(',')
    print(values)

    # If our header has not been read yet, set our headers to a header
    # varianble for later use
    if header == None:
        header = values
    # if our header has been read we want to put this line into our data matrix.
    else:
        data.append(values)

# Now we have our data and we can do whatever we like with it!
print(data)
###
# Problem 2. What is the average height in our dataset?
print("\nPROBLEM 2!\n")

# We can use what we've learnt previously, we can use Numpy's mean() function for this!
import numpy as np

# But that function only finds the mean across a list? Therefore, how do we get a nice list
# of just the ages from our data?

# A naive approach would be to make a new list, and iterate through the data and 
# get the age column (column 2) from each row, and put it into the list:
ages = []
for row in data:
    # By default our file reading program does not automatically interpret the type
    # of our data, as such we need to convert our data into the right type
    # for age, the data should be an integer.
    # we can convert between data types using int(x) to convert x to an integer
    # or str(x) to convert x to a string.

    age = int(row[2])
    ages.append(age)

print("Ages:")
print(ages)
print("Mean:", np.mean(ages))

###

# Problem 3. The same thing but way easier.
print("\nPROBLEM 3!\n")

# The above methods are annoying and tedious though, so we can use
# PANDAS to make our lives way easier.
# First step is to import Pandas, and give it a shorter name (pd) so we can
# call on it faster and easier in our code
import pandas as pd

# Read csv file 
# By default, Pandas will read the CSV file into an object called a "Data Frame"
# which is just a matrix with useful functions for querying, searching, and accessing
# the underlying data.
data = pd.read_csv("ex8.csv")
print(data)

# Pandas will also automatically infer data types for you, making things much more straight forward.

# We can now access our data by referring to column names
# by default, when we call $ data['age'] pandas will return a subset dataframe with the id column
# still attached. To make it a simple list which is easier to work with, we can cast it to a list
# like we did previously with int(). This will make it a simple primitive list just of the ages
# from the dataset.
ages = list(data['age'])
print("Ages:", ages)
print("Mean:", np.mean(ages))

###

# Problem 4. Find the average height for each sex.
print("\nPROBLEM 4!\n")

# We can find a subset of our data easily using list notation:
# data['sex'] returns the data with only the id and sex columns
# we can then check if the sex is equal to 'F' by using ==.
# It follows then that: data['sex'] == 'F', builds a list of which rows have a sex equal to 'F'
# Then we can select those rows by using list selection same as previous: data[x]
females = data[ data['sex'] == 'F' ]
print(females)

# Then we can find the average height in the same manner as in problem 3.
print("Average female height:", np.mean(females['height']))

# This can be condensed into a single line if you fancy it:
print("Average female height (single line):", np.mean(data[ data['sex'] == 'F' ]['height']))

# While this might work for small datasets where you have fairly easy categories like sex, where
# you only have a few sexes (male, female, intersex). In more complex cases you may have many
# categories, and manually calculating each one can be tedious.

# What we can do is first find all the unique values in the sex column, and finding the mean
# across each sex automatically.

# Step 1. find unique values in column
sexes = data["sex"].unique()
print("Unique sexes:", sexes)

# Step 2. iterate through the list of sexes, 
for sex in sexes:
    # Step 3: find the average
    mean_height = np.mean(data[ data['sex'] == sex ]['height'])
    # Step 4: print it out
    print(f"Average height for sex: {sex} = {mean_height}")


print()

# All of this can be combined into a single line if you hate yourself enough to write
# super hard to read code.
print("One liner")
for sex in data["sex"].unique(): print(f"Average height for sex: {sex} = {np.mean(data[ data['sex'] == sex ]['height'])}") 
