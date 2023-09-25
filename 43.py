import turtle
import random

turtle.pensize(3)
for i in range(0, 8):
    turtle.color(random.choice(["Red", "Blue", "Yellow", "Green"]))
    turtle.forward(50)
    turtle.right(45)
turtle.exitonclick()
