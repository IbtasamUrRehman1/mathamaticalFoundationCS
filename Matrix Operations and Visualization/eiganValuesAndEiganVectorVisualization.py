import numpy as np
import matplotlib.pyplot as plt


def calculate_eigenvalues_eigenvectors_visualization(matrix):
    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    # Print eigenvalues and eigenvectors
    print("Eigenvalues :", eigenvalues)
    print("Eigenvectors :")
    for i in range(len(eigenvectors)):
        print(f"Eigenvector {i + 1}:", eigenvectors[:, i])

    # Plotting
    plt.figure(figsize=(10, 5))

    # Plot eigenvalues
    plt.subplot(1, 2, 1)
    plt.plot(eigenvalues, 'bo')
    plt.title('Eigenvalues')
    plt.xlabel('Index')
    plt.ylabel('Value')

    # Plot eigenvectors
    plt.subplot(1, 2, 2)
    for i in range(len(eigenvectors)):
        plt.plot(eigenvectors[:, i], label=f'Eigenvector {i + 1}')
    plt.title('Eigenvectors')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()

    plt.tight_layout()
    plt.show()


# Example
matrix = np.array([[1, 2], [2, 1]])
calculate_eigenvalues_eigenvectors_visualization(matrix)
