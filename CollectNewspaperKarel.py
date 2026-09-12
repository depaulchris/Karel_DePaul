from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

def turn_right():
    """
    Turns Karel right by turning left three times
    """
    for _ in range(3):
        turn_left()

def move_to_door():
    """
    Moves Karel to the door
    """
    for _ in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()

def pick_up_newspaper():
    """
    Picks up the newspaper (beeper)
    """
    if beepers_present():
        pick_beeper()

def turn_around():
    """
    Turns Karel around by turning left twice
    """
    for _ in range(2):
        turn_left()

def return_to_start():
    """
    Returns Karel to the starting position
    """
    turn_around()
    for _ in range(3):
        move()
    turn_right()
    move()
    turn_right()


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_to_door()
    pick_up_newspaper()
    return_to_start()



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
