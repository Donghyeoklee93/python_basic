# built-in modules
#: modules that are automatically installed with Python

from math import pi, ceil as c
print(pi)
print(c(2.7))

# external modules
#: modules that other person made, which is installed by pip
# pyautogui

import pyautogui as pg

pg.moveTo(500, 500, duration=2)