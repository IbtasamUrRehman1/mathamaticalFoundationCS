import numpy as np
import matplotlib.pyplot as plt

def inversionMatrixVisualization(A,b): # calculate the inverse of the coefficient matrix
    A_inv = np.linalg.inv(A)

    # calculate the solution vector
    x = np.dot(A_inv, b)

    # plotting
    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.imshow(A, cmap='viridis')
    plt.colorbar()
    plt.title('Coefficient Matrix (A)')

    plt.subplot(1,2,2)
    plt.plot(b, 'bo-', label='Dependent Variavle (b)')
    plt.plot(x, 'ro-', label='Solution (x)')
    plt.legend()
    plt.title('Solution Vector')

    plt.tight_layout()
    plt.show()

    return x

# Example
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])

solution = inversionMatrixVisualization(A,b)
print("Solution :", solution)










