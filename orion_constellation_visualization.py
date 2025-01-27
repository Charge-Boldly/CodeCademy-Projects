# Import internal library
import codecademylib3

# 1
# Import libraries and modules
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2
# View given x, y, z coordinates
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32, -0.50, -0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25, 13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25, 1.38]

# Print x, y, z to understand ranges
print("X Coordinates:", x)
print("Y Coordinates:", y)
print("Z Coordinates:", z)

# 3
# Create a 2D plot of the Orion constellation
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='white', edgecolor='black')
plt.title('Orion Constellation - 2D')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.gca().set_facecolor("black")
plt.show()

# 4
# Create a 3D plot of the Orion constellation
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='white', edgecolor='black')
ax.set_title('Orion Constellation - 3D')
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')
ax.set_facecolor("black")
plt.show()

# 5
# Night sky scatter plot - 2D
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='yellow', edgecolor='white')
plt.title('Orion Constellation - Night Sky (2D)')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.gca().set_facecolor("black")
plt.show()

# Night sky scatter plot - 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='yellow', edgecolor='white')
ax.set_title('Orion Constellation - Night Sky (3D)')
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')
ax.set_facecolor("black")
plt.show()
