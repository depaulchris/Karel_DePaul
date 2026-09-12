from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

class StoneMasonKarel:
    def __init__(self):
        self.descent = False
        self.beepers = False
        self.run()
    
    def descend(self):
        while(front_is_clear()):
            self.beeper_check()
            move()
        if (front_is_blocked()):
            self.beeper_check()
            self.beepers = self.beepers = False
            turn_left()
            if (front_is_blocked()):
                return
            move()
            turn_left()
            self.ascend()

    def ascend(self):
        self.descent = False
        while(front_is_clear()):
            if (beepers_present()):
                self.beepers = True
            move() 
        if front_is_blocked():
            self.descent = True
            self.turn_around()
            self.descend()

    def turn_around(self):
        for i in range (0,2):
            turn_left()

    def beeper_check(self):
        if (self.beepers):
            if (no_beepers_present()):
                put_beeper()

    def run(self):
        turn_left()
        self.ascend()

def main():
    """
    The code below initializes the StoneMasonKarel class.
    """
    game = StoneMasonKarel()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
