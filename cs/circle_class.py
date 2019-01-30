import math

# Create a class called circle
class Circle:
    # Circle with radius, area, and diameter
    # Solution stolen from Python morsels
    def __init__(self, radius): # Define function, have to have def __init__(self, THING YOU WANT TO DO SOMETHING)
        self.radius = radius # This is saying, when you call something, the radius attribute is the radius
        self.area = math.pi * self.radius ** 2 # Then get area with doing something to the radius value
        self.diameter = self.radius * 2 # Etc.
    def __repr__(self):
        return f'Circle({self.radius})'
c = Circle(1)
c
c.radius
c.area
c.diameter

# As said in Python morsels: "This answer is missing two features that we need: it doesn't default the radius value to 1
# (radius is required) and it doesn't have a useful string representation."
# Why do we need string representation?

# Oh! Because when we just call c we get "<circle.Circle object at 0x7f75816c48d0>"
# Which is not very useful. So we add __repr__ method.
