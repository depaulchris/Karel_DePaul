from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

def move_karel():
    while front_is_clear():
        for i in range(2):
            if front_is_blocked():
                turn_around()
                beeper_cleaner()
                #move_karel_at_wall()
            move()
        turn_around()
        move()
        put_beeper()
        turn_around()

def move_karel_at_wall():
    turn_around()
    while front_is_clear() and no_beepers_present():
        move()
    if beepers_present():
        pick_beeper()
        move()
        beeper_cleaner()

def beeper_cleaner():
    while front_is_clear() and no_beepers_present():
        move()
    pick_beeper()
    move()
    if beepers_present():
        while beepers_present():
            move()
        turn_around()
        move()
        beeper_cleaner()



def beeper_check():
    if no_beepers_present():
        put_beeper()

def turn_around():
    for i in range(2):
        turn_left() 

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_karel()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program("8x8.w")
