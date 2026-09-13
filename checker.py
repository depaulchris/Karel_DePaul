from karel.stanfordkarel import *

def beeper_check():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def change_row():
    if facing_east():
        turn_left()
        if front_is_clear():
            move_left()
    else:
        turn_right()
        if front_is_clear():
            move_right()

def move_left():
    if beepers_present():
        move()
        turn_left()
        if front_is_clear():
            move() 
    else:
        move()
        turn_left()

def move_right():
    if beepers_present():
        move()
        turn_right()
        if front_is_clear():
            move()
    else:
        move()
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def main():
    """
    The code below checks for the 1x1 and 1x8 edge cases and executes the default program if the 
    world doesnt meet the conditions.
    """
    if facing_east() and not right_is_clear() and not left_is_clear() and not front_is_clear():
           put_beeper()
    else:
        if not front_is_clear():
            turn_left()
            if not right_is_clear() and not left_is_clear():
                beeper_check()
        else:
            while front_is_clear():
                beeper_check()
                change_row()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program("40x40.w")
