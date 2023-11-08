# Entire CODE:

from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()  # Lift the pen to move to the starting point
        # Move to the starting position
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()  # Lower the pen to start drawing

        width_rec = abs(self.point1.x - self.point2.x)
        height_rec = abs(self.point1.y - self.point2.y)

        canvas.forward(width_rec)
        canvas.left(90)
        canvas.forward(height_rec)
        canvas.left(90)
        canvas.forward(width_rec)
        canvas.left(90)
        canvas.forward(height_rec)


class GuiPoint(Point):

    def draw(self, canvas, size=5, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
                             Point(randint(10, 400), randint(10, 400)))


# Create rectangle object
rectangle = Rectangle(Point(randint(0, 400), randint(0, 400)),
                      Point(randint(10, 400), randint(10, 400)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_gui_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ",
      user_gui_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

screen = turtle.Screen()
screen.title("Drawing Shapes")
canvas_turtle = turtle.Turtle()
gui_rectangle.draw(canvas=canvas_turtle)
user_gui_point.draw(canvas=canvas_turtle)

screen.exitonclick()
