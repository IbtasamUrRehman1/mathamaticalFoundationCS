import numpy as np
import matplotlib.pyplot as plt


def svd(matrix):
    """
    Singular value decomposition ( SVD ) of a matrix

    :arg:
        -  Matrix Input matrix ( 2D Numpy Array)
    :param matrix:
    :return:
      - U : Left singular vector
      - S: Singular values
      - Vt : Right singular vectors ( transposed)
    """
    U, S, Vt = np.linalg.svd(matrix)
    return U, S, Vt


def plotSvd(U, S, Vt):
    """
    Plots the singular vectors and singular vlaues
    :arg :
      - U : left singular vectors
      - V : Right singular vectors  (transpose)
    -  S: singular values
    """
    plt.figure(figsize=(10, 4))

    plt.subplot(121)
    plt.plot(U[:, 0], U[:, 1], 'ro')
    plt.title("Left Singular Vectors")
    plt.xlabel("First Singular Vectors")
    plt.ylabel("Second Singular Vectors")

    plt.subplot(122)
    plt.bar(np.arange(len(S)), S)
    plt.title("Singular Values")
    plt.xlabel("Index")
    plt.ylabel("Values")

    plt.show()
    print("Left Singular Vectors ( U ):\n ", U)
    print("Singular Vectors ( S ):\n ", S)
    print("Right Singular Vectors ( Vt ):\n ", Vt)


# Example Matrix
matrix = np.array([[1, 2], [3, 4], [5, 6]])
U, S, Vt = svd(matrix)
plotSvd(U, S, Vt)
