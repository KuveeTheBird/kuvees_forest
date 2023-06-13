from src.scene.scene import *
from src.terminal.utils import *
from time import sleep

default_scene = Scene(1, 'Scene 1 descrption')

clear_terminal()

welcome_msg = 'Welcome To Kuvee\'s Forest!'
slow_typing(welcome_msg)

sleep(2)

clear_terminal()
default_scene.show_description()
