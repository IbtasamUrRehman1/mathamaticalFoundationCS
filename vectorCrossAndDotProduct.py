import math
import matplotlib.pyplot as plt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

    def plot(self, color='r', label='Vector'):
        plt.plot([0,self.x], [0,self.y], color + '-', label=label)
        plt.plot(0,0,'ko') # origin
        plt.plot(self.x, self.y, 'bo') # endpoint

v1 = Vector(2,5)
v2 =Vector(-1, 2)

# plotting vectors
plt.figure()
v1.plot(color='r', label='Vector 1')
v2.plot(color='g', label='Vector 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Vector Visualization')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# Dot Product
dot_product = v1.dot_product(v2)
print("Dot Product: ", dot_product)

# Cross Product
cross_product = v1.cross_product(v2)
print("Cross Product: ", cross_product)







