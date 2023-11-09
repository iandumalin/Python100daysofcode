from turtle import Turtle, Screen, colormode

turtle = Turtle()
turtle.speed(0)
turtle.penup()
turtle.goto(0, 500)
turtle.pendown()
colormode(255)

def drawpolygon(sides: int) -> None :
    for _ in range(sides) :
        turtle.right(360/sides)
        turtle.forward(33)
color = 0
polygon = 3
    
while True == True :
    turtle.pencolor(color, 0, color)
    drawpolygon(polygon)
    color += 5
    polygon += 1
    if color > 255 : color = 0

main_screen = Screen()
main_screen.exitonclick()