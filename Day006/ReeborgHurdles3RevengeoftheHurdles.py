# exercise at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle3.json
def jump() :
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
   
def turn_right() :
    turn_left()
    turn_left()
    turn_left()

while not at_goal() :
    if front_is_clear() :
        move()
    elif wall_in_front() :
        jump()