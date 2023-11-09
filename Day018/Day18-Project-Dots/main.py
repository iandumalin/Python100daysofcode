from turtle import Turtle, Screen, colormode
from random import choice
import colorgram
debug = True

colors = colorgram.extract("C:\\Users\\ian.dumalin\\Python100daysofcode\\Day018\\Day18-Project-Dots\\azvtxcls.png", 10)
color_list = []
for color in colors :
    color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    if color_tuple[0] < 250 and color_tuple[1] < 250 and color_tuple[2] < 250 :
        color_list.append(color_tuple)
    
if (debug) : print (color_list)

turtle = Turtle()
turtle.speed(5)
turtle.penup()
turtle.hideturtle()
colormode(255)
turtle_X = -300
turtle_y = -300
turtle.setposition(turtle_X, turtle_y)

def create_orb(color_tuple) :
    turtle.dot(30, color_tuple)
    
def create_row(number_of_orbs) :
    for _ in range(number_of_orbs) :
        create_orb(choice(color_list))
        turtle.forward(50)
        
for _ in range(10) :
    create_row(10)
    turtle_y += 50
    turtle.setposition(turtle_X, turtle_y)

main_screen = Screen()
main_screen.exitonclick()