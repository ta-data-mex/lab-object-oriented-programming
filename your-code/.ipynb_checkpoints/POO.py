import numpy as np
import operator
def twodim(mat):
    len_mat = len(mat)
    if len_mat == 1:
        return 'Matriz de 1 elemento'
    elif len_mat == 2:
        return 'Matriz de 2 elementos'
    elif len_mat == 3:
        return 'Matriz de 3 elementos'


def twodim_recursivo(mat1):
    len_mat1 = len(mat1)
    while len_mat1 < 1:
        len_mat1 = len_mat1 + 1
    return len_mat1


# Next, we will write a function that checks for the number of rows and columns of a matrix.
# Recall that the outer list will tell us the number of rows and the inner lists will tell us the number of columns.
# Make sure that all inner lists are of the same length.
def rowcolumn(mat):
    cont_col, cont_row = 0, 0
    cont_col2 = 0
    for x in mat:
        cont_row = cont_row+1
        for y in x:
            cont_col = cont_col + 1
            cont_col2 = cont_col/cont_row

    return cont_row, cont_col2


def compare(mat1, mat2):
    for x in mat1:
        print(x)
        for y in mat2:
            print(y)

#print(compare([[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]))

    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a)


def addition(mat1, mat2):

    # This function takes a two lists of lists and adds each cell together
    # Input: two list of lists
    # Output: one summed list of lists
    #
    # Sample input: [[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]
    # Sample Output: [[8,10,12],[14,16,18]]

    # Your code here:
    add = [[0, 0, 0], [0, 0, 0]]
    for x in range(len(mat1)):
        for y in range(len(mat1[0])):
            add[x][y] = mat1[x][y] + mat2[x][y]
    return add


#print(addition([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]))


class Matrix2D:
    # First, we will write the __init__ function.
    # In this function, we will initialize rows and the columns using the matrix that we have passed to the class.

    def __init__(self, mat):
        self.mat = mat
        self.row = self.rowcolumn()
        self.col = self.rowcolumn()
# Assign mat to self.mat
# Assign rows and cols to self.rows and self.cols
# To find the rows and the cols, use the rowcolumn function and pass self.mat to the function.
# Since the rowcolumn function is now a member of the class, make sure to refer to the function as self.rowcolumn

# Your code here:


# Insert the twodim function here.
# The only change you need to make is that now we are passing self and mat to the function (make sure self is first).

# Your code here:
    def twodim(self, mat):
        len_mat = len(mat)
        if len_mat == 1:
            return 'Matriz de 1 elemento'
        elif len_mat == 2:
            return 'Matriz de 2 elementos'
        elif len_mat == 3:
            return 'Matriz de 3 elementos'

# Insert the rowcolumn function here.
# The changes you need to make:
# 1. The function now takes self and mat as arguments (make sure to pass self first).
# 2. Any reference to twodim will be changed to self.twodim since this function is a member of the class and takes self

# Your code here:
    def rowcolumn(self, mat):
        cont_col, cont_row = 0, 0
        cont_col2 = 0
        for x in mat:
            cont_row = cont_row + 1
            for y in x:
                cont_col = cont_col + 1
                cont_col2 = cont_col / cont_row

        return cont_row, cont_col2


# Insert the compare function here
# Add self as the first argument passed to the function

# Your code here:
    def compare(self, mat1, mat2):

        # This function takes a two lists of lists and checks whether they have the same number of rows and columns
        # Input: two list of lists
        # Output: True or False
        #
        # Sample input: [[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]
        # Sample Output: True

        # Your code here:
        len_mat1 = len(mat1)
        len_mat2 = len(mat2)
        if len_mat1 == len_mat2:
            return True
        else:
            return False


# Insert the addition function here
# This function now takes self and matrix (another matrix of the Matrix2D class)
# Change the compare function to self.compare
# Change any reference to mat1 and mat2 to self.mat and matrix.mat respectively
# Return your result as a Matrix2D(result). This will ensure that we return a new matrix and not a list of lists.

# Your code here:

    def addition(self, mat1, mat2):
        add = [[0, 0, 0], [0, 0, 0]]
        for x in range(len(mat1)):
            for y in range(len(mat1[0])):
                add[x][y] = mat1[x][y] + mat2[x][y]
        return add

        return Matrix2D







