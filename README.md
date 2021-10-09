Have you ever tried updating the terminal with text that changes multiple times a second? Remember how when you tried clearing the console with os.system calls it would make the console flash and make the text unreadable? I wrote this python module to prevent exactly that. Introducing...

# ConsoleDraw
A python module to update the console without flashing.

# Supported Operating Systems
The consoledraw module should be supported on Windows, Linux and Mac (although it has not been tested on Mac).

# Installation
This python package can be installed using pip.
```
pip install consoledraw
```

# Demo
demo.py:
```python
from math import sin
from time import sleep

import consoledraw

console = consoledraw.Console()

x = 0
while True:
    console.clear() # Clears the custom console's buffer
    
    for i in range(23):
        console.print("    |" + " " * round(abs(sin((x + i) * 0.05)) * 9.5) + "O") # Prints to the custom console's buffer (works the same as python's built-in print)
    
    console.update() # Draws the custom console's buffer to the screen
    
    x += 1

    sleep(1/60) 
```
![Demo GIF](https://media0.giphy.com/media/gXfAUJAD8hHwBcJIFP/giphy.gif?cid=790b7611aab0b776e0e3796d1e0e0e60f7012fc4300d0b9e&rid=giphy.gif&ct=g)
