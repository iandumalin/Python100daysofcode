from turtle import Turtle, Screen, colormode
from random import choice

turtle = Turtle()
colormode(255)
turtle.pensize(10)
turtle.speed(0)
color_tuple = (
    (choice(range(150, 256)), choice(range(150, 256)), choice(range(150, 256))),
    (choice(range(150, 256)), choice(range(150, 256)), choice(range(150, 256))),
    (choice(range(150, 256)), choice(range(150, 256)), choice(range(150, 256))),
    (choice(range(150, 256)), choice(range(150, 256)), choice(range(150, 256))),
    (choice(range(150, 256)), choice(range(150, 256)), choice(range(150, 256)))
)
direction_tuple = (0, 90, 180, 270)

while True == True :
    turtle.pencolor(choice(color_tuple))
    turtle.setheading(choice(direction_tuple))
    turtle.forward(20)

main_screen = Screen()
main_screen.exitonclick()