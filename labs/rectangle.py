class Rectangle:
    # Constructor
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # Calculate the area
    def area(self):
        return self.height * self.width
    # Calculate the perimeter
    def perimeter(self):
        return (self.height * 2) + (self.width * 2)

# Create instance
r1 = Rectangle(10, 35)
r1.height = 20

# Another instance
r2 = Rectangle(2, 5)

print(f"Area of r1 = {r1.height} x {r1.width} = {r1.area()}")
print(f"Area of r2 = {r2.height} x {r2.width} = {r2.area()}")
print(f"Perimeter of r1 = {r1.height} x {r1.width} = {r1.perimeter()}")
print(f"Perimeter of r2 = {r2.height} x {r2.width} = {r2.perimeter()}")

