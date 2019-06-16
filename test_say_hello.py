"""Test cases for brisk

Unit tests that covers brisk cababilities.

To run:
    $ pytest test_say_hello.py
"""
from main import say_hello

def test_say_hello_does_not_print_bye(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert 'bye' not in  captured.out