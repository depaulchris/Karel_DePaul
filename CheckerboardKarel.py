from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

def move_right():
    if facing_east() and not right_is_clear() and not left_is_clear() and not front_is_clear():
        print("wtf")
        put_beeper()
    else:
        if not front_is_clear():
            turn_left()
            if not right_is_clear() and not left_is_clear():
                while front_is_clear():
                    for i in range(4):
                        if front_is_clear():
                            if i % 2 == 0:
                                put_beeper()
                            move()
                        else: 
                            if i % 2 == 0:
                                put_beeper()
                            turn_left()
        else:
            while front_is_clear():
                for i in range(100):
                    if front_is_clear():
                        if i % 2 == 0:
                            put_beeper()
                        move()
                    else: 
                        if facing_east():
                            if i % 2 == 0:
                                put_beeper()
                            turn_left()
                            if front_is_clear():
                                move()
                                turn_left()
                                if (i + 1) % 2 != 0:
                                    move_left_odd()
                                else:
                                    move_left()

def move_left_odd():
    while front_is_clear():
        for i in range(100):
            if front_is_clear():
                if i % 2 != 0:
                    put_beeper()
                move()
            else:
                if right_is_clear() and left_is_clear():
                    turn_around_left()
                    move()
                    turn_around_left()
                    move_right()

def move_left():
    while front_is_clear():
        for i in range(100):
            if front_is_clear():
                if i % 2 == 0:
                    put_beeper()
                move()
            else:
                if right_is_clear() and left_is_clear():
                    turn_around_left()
                    move()
                    turn_around_left()
                    move_right()

def turn_around_left():
    for i in range (3):
        turn_left()

def run():
    move_right()

def main():
    """
    The code below uses the run function to begin the program.
    """
    run()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program("8x1.w")
    #run_karel_program("")
