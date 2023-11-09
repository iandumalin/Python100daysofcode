from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(1)
for i in range(4) :
    turtle.right(90)
    turtle.forward(100)
main_screen = Screen()
main_screen.exitonclick()