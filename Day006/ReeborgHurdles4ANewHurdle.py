# exercise at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle4.json
def jump() :
    over_hurdle = False
    while not over_hurdle :
        turn_left()
        move()
        turn_right()
        if front_is_clear() :
            over_hurdle = True
    if over_hurdle :
        move()
        turn_right()
        while front_is_clear() :
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