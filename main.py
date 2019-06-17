"""Brisk main script

This is the script of brisk. A program that always happy and say only \n
hello and only hello.Unfortunately it works for 1 minute only so run \n
it again if you like it.

Example:
    $ python3 main.py

This script contains the following functions:
    * say_hello()

"""

import time
import os

TIME_TO_SLEEP = 5
TOTAL_TIME_TO_WORK = 60


def say_hello():
    """Print hello for one minute every five seconds.."""
    time_elapsed = 0
    while time_elapsed <= TOTAL_TIME_TO_WORK:
        print('hello2')
        time.sleep(TIME_TO_SLEEP)
        time_elapsed += TIME_TO_SLEEP


if __name__ == '__main__':
    say_hello()
