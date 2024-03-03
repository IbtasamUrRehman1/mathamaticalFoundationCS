import numpy as np
import matplotlib.pyplot as plt

# Define matrices A and B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix Addition
addition_matrix = A + B

# Matrix Subtraction
subtraction_matrix = A - B

# Matrix Multiplication
multiplication_matrix = A * B

# Transpose of Matrix A
transpose_A = np.transpose(A)

# Transpose of Matrix B
transpose_B = np.transpose(B)

# Print results
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Addition (A + B):\n", addition_matrix)
print("Matrix Subtraction (A - B):\n", subtraction_matrix)
print("Matrix Multiplication (A * B):\n", multiplication_matrix)
print("Transpose of Matrix A:\n", transpose_A)
print("Transpose of Matrix B:\n", transpose_B)

# Plotting
plt.figure(figsize=(10, 6))

# plot of matrix A
plt.subplot(2, 3, 1)
plt.imshow(A, cmap='viridis')
plt.colorbar()
plt.title('Matrix A')

# plot the matrix Addition
plt.subplot(2, 3, 2)
plt.imshow(addition_matrix, cmap='viridis')
plt.colorbar()
plt.title('Matrix B')

# plot the matrix Addition
plt.subplot(2, 3, 3)
plt.imshow(addition_matrix, cmap='viridis')
plt.colorbar()
plt.title('Matrix Addition ( A + B)')

# plot the matrix subtraction
plt.subplot(2, 3, 4)
plt.imshow(subtraction_matrix, cmap='viridis')
plt.colorbar()
plt.title('Matrix Subtraction ( A - B)')

# Plot the transpose of Matrix A
plt.subplot(2, 3, 5)
plt.imshow(transpose_A, cmap='viridis')
plt.colorbar()
plt.title('Transpose of Matrix A')

# plot the transpose of Matrix B
plt.subplot(2, 3, 6)
plt.imshow(transpose_B, cmap='viridis')
plt.colorbar()
plt.title('Transpose of Matrix B')
plt.tight_layout()
plt.show()
