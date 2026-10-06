# Polymorphism
# Poly means many, morph means forms. Polymorphism allows the same method name to behave differently depending on which object calls it. This makes your code highly flexible and extensible.

# Same method name works differently for different classes
# You don't need to remember multiple method names for similar actions
# Method Overriding: Child class provides its own version of a parent's method

# Real life example: A "draw()" method on a Circle draws a circle, on a Rectangle it draws a rectangle
# different behavior
# same name,


class Shape:
    def draw(self):
        # Default method to be overridden by child classes
        print("Drawing a generic shape")

class Circle(Shape):
    def draw(self):
        # Overriding the parent method for unique behavior
        print("Drawing a Circle 🔴")

class Rectangle(Shape):
    def draw(self):
        # Overriding the parent method for unique behavior
        print("Drawing a Rectangle 🟦")


def render_shape(shape_obj):
    
    shape_obj.draw()

my_circle = Circle()
my_rectangle = Rectangle()


render_shape(my_circle)     
render_shape(my_rectangle)  
