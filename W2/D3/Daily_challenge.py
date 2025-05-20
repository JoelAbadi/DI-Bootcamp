import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must specify either a radius or a diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

#Test the Circle class below


c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=3)
c4 = Circle(radius=7)

print("Circle 1:", c1)
print("Circle 2:", c2)
print("Circle 3:", c3)
print("Circle 4:", c4)

print("\nAreas:")
print("Area of c1:", c1.area)
print("Area of c2:", c2.area)

c5 = c1 + c3
print("\nNew circle from c1 + c3:", c5)

print("\nComparisons:")
print("Is c1 > c3?", c1 > c3)
print("Is c1 == c2?", c1 == c2)
print("Is c4 < c5?", c4 < c5)

circles = [c1, c2, c3, c4, c5]
sorted_circles = sorted(circles)

print("\nSorted Circles by radius:")
for circle in sorted_circles:
    print(circle)



# Bonus: Draw the circles with Turtle


def draw_circles(circle_list):
    screen = turtle.Screen()
    screen.title("Sorted Circles")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    x = -300  

    for circle in circle_list:
        t.goto(x, 0 - circle.radius)  
        t.pendown()
        t.circle(circle.radius)
        t.penup()
        x += circle.diameter + 20  

    turtle.done()
