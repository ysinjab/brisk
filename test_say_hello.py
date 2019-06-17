"""Test cases for brisk

Unit tests that covers brisk cababilities.

To run:
    $ pytest test_say_hello.py
"""
import main
from main import say_hello


def test_say_hello_does_not_print_bye(capsys, monkeypatch):
    monkeypatch.setattr(main, 'TOTAL_TIME_TO_WORK', 2, raising=True)
    monkeypatch.setattr(main, 'TIME_TO_SLEEP', 1, raising=True)
    say_hello()
    captured = capsys.readouterr()
    assert 'bye' not in captured.out
