import numpy as np
from scipy import linalg

# We are trying to solve a linear algebra system which can be given as
#         x + 3y +10z = 10
#         2x + 12y + 7z = 18
#         5x + 8y + 8z = 30
# Creating input array
A = np.array([[1, 3, 10], [2, 12, 7], [5, 8, 8]])
# Solution Array
B = np.array([[10], [18], [30]])
# Solve the linear algebra
X = linalg.solve(A, B)
# Print results
print(X)
# Checking Results
print("\n Checking results, Vectors must be zeros")
print(A.dot(X) - B)

#Determinant

#Declaring the numpy array
A = np.array([[5,9],[8,4]])
#Passing the values to the det function
x = linalg.det(A)
#printing the result
print(x)


#Eigenvalues and eigenvectors

#Declaring the numpy array
a = np.array([[3,2],[4,6]])
#Passing the values to the eig function
l, v = linalg.eig(a)
#printing the result for eigenvalues
print(l)
#printing the result for eigenvectors
print(v)

#QR factorization
a = np.array([[3,2],[4,6]])
Q,R=linalg.qr(a)
print('Q:',Q,sep='\n')
print('R:',R,sep='\n')

# LU decomposition

#Define a square matrix
a = np.array([[1, 2], [3, 4]])

# Compute the LU decomposition
P, L, U = linalg.lu(a)

# Print the results
print("Permutation matrix P:", P,sep='\n')
print("Lower triangular matrix L:", L,sep='\n')
print("Upper triangular matrix U:", U,sep='\n')



#Single value decomposition
a = np.array([[3,2],[4,6]])
x=linalg.svd(a=a)

print(x)
for it in x:
    print('*****')
    print(it)