from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed(1)

for _ in range(10) :
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    
    
main_screen = Screen()
main_screen.exitonclick()