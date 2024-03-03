import numpy as np
import matplotlib.pyplot as plt


def gaussian_elimination_visualization(A, b):
    """
    Solve the system of linear equations Ax = b using Gaussian elimination with visualization.

    Parameters:
        A (ndarray): Coefficient matrix of shape (n, n).
        b (ndarray): Dependent variable vector of shape (n,).

    Returns:
        x (ndarray): Solution vector of shape (n,).
    """
    n = len(b)
    # Convert all elements to float for consistent dtype
    A = A.astype(float)
    b = b.astype(float)
    # Augmented matrix
    aug_matrix = np.hstack((A, b.reshape(n, 1)))

    # List to store augmented matrices for visualization
    augmented_matrices = [aug_matrix.copy()]

    # Forward Elimination
    for pivot_row in range(n - 1):
        for row in range(pivot_row + 1, n):
            factor = aug_matrix[row][pivot_row] / aug_matrix[pivot_row][pivot_row]
            aug_matrix[row][pivot_row:] -= factor * aug_matrix[pivot_row][pivot_row:]
            augmented_matrices.append(aug_matrix.copy())

    # Back Substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (aug_matrix[i][-1] - np.dot(aug_matrix[i][i + 1:n], x[i + 1:n])) / aug_matrix[i][i]

    return x, augmented_matrices


# Example
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])

solution, augmented_matrices = gaussian_elimination_visualization(A, b)
print("Solution:", solution)

# Plotting augmented matrices
fig, axes = plt.subplots(1, len(augmented_matrices), figsize=(len(augmented_matrices) * 5, 5))
for i, augmented_matrix in enumerate(augmented_matrices):
    ax = axes[i]
    ax.imshow(augmented_matrix, cmap='viridis')
    ax.set_title(f"Step {i + 1}")
    ax.set_xlabel('Columns')
    ax.set_ylabel('Rows')
    ax.set_xticks(np.arange(len(augmented_matrix[0])))
    ax.set_yticks(np.arange(len(augmented_matrix)))
    ax.grid(color='w', linestyle='-', linewidth=1)
plt.tight_layout()
plt.show()
