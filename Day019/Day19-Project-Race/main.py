from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)
race_ongoing = False

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Go ahead and bet" , prompt="Which turtle color will win the race? : ")
turtle_list = []
color_tuple = (
    "red",
    "orange",
    "cyan", 
    "blue",
    "green",
    "purple"
)
y_tuple = (-100, -60, -20, 20, 60, 100)
print(user_bet)

for turtle_range in range(0, 6) :
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color_tuple[turtle_range])
    turtle.goto(x=-230, y=y_tuple[turtle_range])
    turtle_list.append(turtle)
    
    
if user_bet :
    race_ongoing = True

while race_ongoing :
    for turtle in turtle_list :
        turtle.forward(choice(range(0, 21)))
        if turtle.xcor() >= 230 :
            race_ongoing = False
            if user_bet == turtle.color()[0] : print("You win!")
            else : print(f"You lose, {turtle.color()[0]} won!")
            break
            

screen.exitonclick()