"""Brisk main script

This is the script of brisk. A program that always happy and say only hello and only hello.
Unfortunately it works for 1 minute only so run it again if you like it.

Example:
    $ python3 main.py

This script contains the following functions:
    * say_hello()

"""
import time

def say_hello():
    """Print hello for one minute every five seconds.."""
    time_elapsed = 0
    while time_elapsed <= 60:
        print('hello')
        time.sleep(5)
        time_elapsed += 5

if __name__ == '__main__':
    say_hello()