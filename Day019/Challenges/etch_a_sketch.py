from turtle import Turtle, Screen

cursor = Turtle()
main_screen = Screen()

def move_forward(paces: int = 10):
    cursor.forward(paces)
def move_backward(paces: int = 10):
    cursor.forward(-paces)
def turn_left() :
    cursor.left(10)
def turn_right() :
    cursor.right(10)
def clearscreen() :
    cursor.penup()
    cursor.clear()
    cursor.home()
    cursor.pendown()

main_screen.listen()
main_screen.onkey(key="z", fun=lambda: move_forward(10))
main_screen.onkey(key="s", fun=lambda: move_backward(10))
main_screen.onkey(key="q", fun=turn_left)
main_screen.onkey(key="d", fun=turn_right)
main_screen.onkey(key="c", fun=clearscreen)

main_screen.exitonclick()