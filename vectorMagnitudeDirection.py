import math
import matplotlib.pyplot as plt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def direction(self): # calculate the andle respect to the positive x-asix
        angle_rad = math.atan2(self.x, self.y)
        # Convert angle from randians to degree
        angle_deg = math.degrees(angle_rad)
        # Ensure the angle is betwee 0 and 36- degree
        if angle_deg < 0:
            angle_deg += 360
        return angle_deg
    def plot(self):
        plt.figure()
        plt.plot([0, self.x], [0, self.y],'r-', label='Vector')
        plt.plot(0,0,'ko') # Origin
        plt.plot(self.x, self.y, 'bo')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Vector Visualization')
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.show()
# Example
v = Vector(8,4)
print('Vector: ', v.x, v.y)
print('Magnitude: ', v.magnitude())
print('Direction: ', v.direction())
v.plot()






