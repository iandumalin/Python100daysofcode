from turtle import Turtle, Screen, colormode
from random import choice

amount_of_circles = 12
circle_radius = 100
color_tuple = (
    (choice(range(150, 256)), choice(range(50, 256)), choice(range(50, 256))),
    (choice(range(150, 256)), choice(range(50, 256)), choice(range(50, 256))),
    (choice(range(150, 256)), choice(range(50, 256)), choice(range(50, 256))),
    (choice(range(150, 256)), choice(range(50, 256)), choice(range(50, 256)))
)
turtle = Turtle()
turtle.speed(0)
turtle.pensize(3)
colormode(255)
color_choice = 0

for _ in range(amount_of_circles) :
#    turtle.pencolor(choice(color_tuple))
#    if turtle.heading() >= 0 : turtle.pencolor(color_tuple[0])
#    if turtle.heading() >= 90 : turtle.pencolor(color_tuple[1])
#    if turtle.heading() >= 180 : turtle.pencolor(color_tuple[2])
#    if turtle.heading() >= 270 : turtle.pencolor(color_tuple[3])
    turtle.pencolor(color_tuple[color_choice])
    color_choice += 1
    if color_choice >= 4 : color_choice = 0
    turtle.circle(100)
    turtle.left(360/amount_of_circles)

main_screen = Screen()
main_screen.exitonclick()