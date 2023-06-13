import os
from random import random
from time import sleep


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def slow_typing(message, typing_speed=0.15):
    for letter in message:
        print(letter, end='')
        sleep(random() * typing_speed)
