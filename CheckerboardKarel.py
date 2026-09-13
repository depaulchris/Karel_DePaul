from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
class CheckerboardKarel:
    def __init__(self):
        self.steps = 0
        self.vertical = False
        self.run()
    
    def move_right(self):
        while front_is_clear():
            self.beeper_check()
            move()
            self.steps += 1
        if front_is_blocked():
            self.vertical = True
            turn_left()
            if self.vertical:
                self.beeper_check(True)
            if front_is_blocked():
                return
            move()
            self.steps += 1
            turn_left()
            self.move_left()

    def move_left(self):
        while front_is_clear():
            self.beeper_check()
            move()
            self.steps += 1
        if front_is_blocked():
            self.turn_around_left()
            if front_is_blocked():
                return
            move()
            self.steps += 1
            self.turn_around_left()
            self.move_right()

    def turn_around_left(self):
        for i in range (0,3):
            turn_left()

    def beeper_check(self, vertical = False):
        if not vertical:
            if (self.steps + 1) % 2 != 0:
                put_beeper()
        else:
            if self.steps % 2 == 0:
                put_beeper()

    def run(self):
        self.move_right()

def main():
    """
    The code below intializes the Checkerboard Karel class and starts the program.
    """
    game = CheckerboardKarel()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
