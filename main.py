import time

def say_hello():
    time_elapsed = 0
    while time_elapsed <= 60:
        print('hello')
        time.sleep(5)
        time_elapsed += 5

if __name__ == '__main__':
    say_hello()