import math
import matplotlib.pyplot as plt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def direction(self): # calculate the angle with respect to the positive x-axis
        angle_rad = math.atan2(self.y, self.x)
        # convert the angle from radian to degrees
        angle_deg = math.degrees(angle_rad)
        # ensure the angle is between 0 and 360 degrees
        if angle_deg < 0:
            angle_rad += 360
        return  angle_deg
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y )
    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def scalar_multiply(self,scalar):
        return Vector(self.x + scalar, self.y * scalar)

    def plot(self, color='r', label='Vector'):
        plt.plot([0, self.x], [0, self.y], color +'-', label=label)
        plt.plot(0,0,'ko') # Origin
        plt.plot(self.x, self.y, 'bo') # Endpoint

# Example
v1 = Vector(3,4)
v2 = Vector(-1, 2)

print("Vector 1: ", v1.x, v1.y)
print("Vector 2: ", v2.x, v2.y)

print("Magnitude of Vector 1: ", v1.magnitude())
print("Magnitude of Vector 2: ", v2.magnitude())

# Vector addition
v_Add = v1.add(v2)
print("Vector Addition: ", v_Add.x, v_Add.y)



# Vector substraction
v_subtract = v1.subtract(v2)
print("Vector Subtraction: ", v_subtract.x, v_subtract.y)

# Scalar multiplicatiomn
scalar = 2
v_scalar_multiply = v1.scalar_multiply(scalar)
print("Scalar Multiplication (by {}:)".format(scalar), v_scalar_multiply.x, v_scalar_multiply.y)

# Plotting
plt.figure()
v1.plot(color='r', label='Vector 1')
v2.plot(color ='g', label='Vector 2')
v_Add.plot(color='b', label='Vector Addition')
v_subtract.plot(color='y', label='Vector Substraction')
v_scalar_multiply.plot(color='m',label='Scalar Multiplication')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vector Operations Visualization')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()





























