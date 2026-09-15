from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

def descend():
    while front_is_clear():
        beeper_check()
    if front_is_blocked():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            ascend()

def ascend():
    while front_is_clear():
        beeper_check()
    if front_is_blocked():
        turn_around()
        descend()

def turn_around():
    for i in range (2):
        turn_left()

def beeper_check():
    if beepers_present():
        move()
        if no_beepers_present():
            while no_beepers_present():
                if front_is_clear():
                    put_beeper()
                    move()
                else:
                    put_beeper()
    else:
        move()
    
def run():
    turn_left()
    ascend()

def main():
    """
    The code below uses the run function to begin the program, which checks for the presence of beepers in both directions.
    """
    run()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program("SampleQuad1.w")
