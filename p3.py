import sys
# Program #3
# Read from a file of matrices, print the matrices, and multiply them together
# CS320-01
# October 09, 2019 
# @author Jason Songvilay cssc0514

# This function begins execution of program.
# Verify data input filename provided on command line: len(sys.argv)
# If error, output message for user: Usage: p3.py dataFileName'
# and quit, using sys.exit()
#
# Declare A, B, call read_matrices to initialize A, B, and store
# return value as C
#
# Print A and B contents
#
# Call mult_matrices
#
# Print result contents
#
def main(): 
  print("Program #3, cssc0514, Jason Songvilay")
  if len(sys.argv) != 2:
    print("Usage: p3.py dataFileName")
    sys.exit()	#if the number of arguments is less than 2, print usage 				#and end the program
  
  A = []
  B = []
  C = read_matrices(A,B) #read in values from file for matrices A, B and set to C

  print("Matrix A contents: ")
  print_matrix(A)
  print("\n")

  print("Matrix B contents: ")
  print_matrix(B)
  print("\n")

  mult_matrices(A,B,C) #multiply matrix A and B together and store in C

  print("Matrix A * B is: ")
  print_matrix(C)

# This function reads m, n, and p from the datafile.
# Then matrices A and B are filled from the datafile.
# Matrix C is then allocated size m x p.
# The values for m, n, and p are local values filled in by this function
# PARAMETERS in order are:
# list matrix A
# list matrix B
# RETURN matrix C
#

def read_matrices(A,B):
  f = open(sys.argv[1], 'r') #open file of matrices
  m = [int(x) for x in next(f).split()][0] #read in row of Matrix A
  n = [int(x) for x in next(f).split()][0] #read in col of Matrix A, row of Matrix B
  p = [int(x) for x in next(f).split()][0] #read in col of Matrix B

  for x in range(m):
    A.append([int(i) for i in next(f).split()]) #fill Matrix A wih row, cols
    
  for x in range(n):
    B.append([int(i) for i in next(f).split()]) #fill Matrix B with A[cols], B[cols]

  C = [[0 for i in range(p)] for j in range(m)] #initialize size of matrix C

  return C #return matrix C

# This function prints a matrix. Rows and columns should be preserved.
# PARAMETERS in order are:
# list The matrix to print
#
def print_matrix(matrix):
  for rows in matrix:
    for cols in rows:
      print('{:3}'.format(cols), end = ' ') #prints formatted matrix spaced by 3
    print("") #start a new column if the end is a space
    

# The two matrices A and B are multiplied, and matrix C contains the
# result.
# PARAMETERS in order are:
# list Matrix A
# list Matrix B
# list Matrix C (all zeros at this point)
#
def mult_matrices(A,B,C):
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        C[i][j] += A[i][k] * B[k][j] #C[i][j] = A[row][col] * B[A[col]][col]
  
# Begin program
if __name__ == '__main__':
  main()
