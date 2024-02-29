import numpy as np
import matplotlib.pyplot as plt


def plotMatrixDeterminent(matrix):
    """
    Plots a matrix with its determinent highlited using matplotlib
    Args: - Matrix to be plotted ( 2D Numpy array)
    """
    det = np.linalg.det(matrix)

    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Value')
    plt.title(f'Matrix Visualization\nDeterminent = {det:.2f}')
    plt.fill_between([-0.5, matrix.shape[1] - 0.5], [-0.5, -0.5], [matrix.shape[0] - 0.5, matrix.shape[0] - 0.5],
                     color='red', alpha=0.5)
    plt.show()


# Example
matrix = np.array([
    [2, 3, 1],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix")
print(matrix)
print("Determinent : ", np.linalg.det(matrix))
plotMatrixDeterminent(matrix)