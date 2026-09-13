from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


#def __init__(self):
#    self.descent = False
#    self.beepers = False
#    self.run()

def descend():
    while front_is_clear():
        if beepers_present():
            move()
            if no_beepers_present():
                while no_beepers_present():
                    if front_is_clear():
                        beeper_check()
                        move()
                    else:
                        beeper_check()
        else:
            move()
    if front_is_blocked():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            ascend()

def ascend():
    while front_is_clear():
        if beepers_present():
            move()
            if no_beepers_present():
                while no_beepers_present():
                    if front_is_clear():
                        beeper_check()
                        move()
                    else:
                        beeper_check()
        else:
            move()
    if front_is_blocked():
        turn_around()
        descend()

def turn_around():
    for i in range (0,2):
        turn_left()

def beeper_check():
    if no_beepers_present():
        put_beeper()

def run():
    turn_left()
    ascend()

def main():
    """
    The code below uses the run function to begin the program.
    """
    run()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
