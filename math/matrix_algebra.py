# Matrix Algebra

import numpy as np

A = np.matrix(((1, 2, 3), (2, 7, 4)))
B = np.matrix(((1, -1), (0, 1)))
C = np.matrix(((5, -1), (9, 1), (6, 0)))
D = np.matrix(((3, -2, -1), (1, 2, 3)))
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.matrix(((1), (8), (0), (5)))

# Question 1.1
print(A.shape)
# (2, 3) or 2 X 3

# Question 1.2
print(B.shape)
# (2, 2) or a 2 X 2

# Question 1.3
print(C.shape)
# (3, 2) or 3 X 2

# Question 1.4
print(D.shape)
# (2, 3) or 2 X 3

# Question 1.5
print(u.shape)
# (4,) as this is an array

# Question 1.6
print(w.shape)
# (1, 4) or 1 X 4

# Question 2.1
print(u + v)
# [9, 7, -4, 9]

# Question 2.2
print(u - v)
# [3, -3, -2, 1]

# Question 2.3
print(6 * u)
# [36, 12, -18, 30]

# Question 2.4
print(np.dot(u, v))
# 51

# Question 2.5
print(np.linalg.norm(u))
# 8.602

# Question 3.1
try:
    A + C
except ValueError:
    print('Question 3.1 not defined')
# Not defined: operands could not be broadcast together with shapes (2,3) (3,2)

# Question 3.2
print(A - np.transpose(C))
# [[-4, -7, -3]
# [3, 6, 4]]

# Question 3.3
print(np.transpose(C) + (3 * D))
# [[14, 3, 3],
# [2, 7, 9]]

# Question 3.4
print(B * A)
# [[-1, -5, -1],
# [2, 7, 4]]

# Question 3.5
try:
    B * np.transpose(A)
except ValueError:
    print('Question 3.5 not defined')
# Not defined: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# Question 3.6
try:
    B * C
except ValueError:
    print('Question 3.6 not defined')
# Not defined: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# Question 3.7
print(C * B)
# [[5, -6],
# [9, -8],
# [6, -6]]

# Question 3.8
print(B ** 4)
# [[1, -4],
# [0, 1]]

# Question 3.9
print(A * np.transpose(A))
# [[14, 28],
# [28, 69]]

# Question 3.10
print(np.transpose(D) * D)
# [[10, -4, 0],
# [-4, 8, 8],
# [0, 8, 10]]
