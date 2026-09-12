from karel.stanfordkarel import * 

"""
File: MoveAndDrop.py
----------------------
Karel starts in the bottom-left corner of the world (1st Street, 1st Avenue), facing east. 
The world is one row high and at least three columns wide. Your job is to make Karel move 
forward two spaces and put down one beeper.

When finished, Karel should be standing on the third corner (Avenue 3), facing east, 
with a beeper on that square.  Use the following world to test your code:
1x8.w
"""


def main():
    """
    The following code moves Karel two spaces to the right and places a beeper in that spot.
    It also initializes the program with a 3 by 1 world as described in the above docstring.
    Running the world with the 1x8.w world causes Karel to crash.
    """
    for i in range(0, 2):
        move()
    put_beeper()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program("3x1.w")
