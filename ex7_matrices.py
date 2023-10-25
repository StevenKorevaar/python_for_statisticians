# It is also possible to make lists of lists, but you can think of these as matrices or tensors if you're fancy
# This is very useful, as most people store data in excel files or CSV files, which can be thought of as 
# 2 dimensional lists: you have rows and columns.

matrix = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14]
]

# To move through them you'll need to use DOUBLE LOOPS!!!! :O :O :O 

for inner_list in matrix:
    for element in inner_list:
        print(element, end=", ")
    print()

print()

# A better way to iterate through matrices is by using indices though

# make an iterator, i, that goes from 0 to the length of the outer most list
for i in range(len(matrix)):
    # make another iterator, j, that goes from 0 to the length of the ith inner list
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=", ")
    print()
