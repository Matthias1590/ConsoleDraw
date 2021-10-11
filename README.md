Have you ever tried updating the console with text that changes multiple times a second? Remember how when you tried clearing the console with os.system calls it would make the console flash and make the text unreadable? I wrote this python module to prevent exactly that. Introducing...

# ConsoleDraw
A python module to update the console without flashing.

# Installation
The consoledraw module can be installed using pip.
```
pip install consoledraw
```
If that doesn't work, try this instead.
```
pip install git+https://github.com/Matthias1590/ConsoleDraw.git
```
Or, if you want to, you can clone the repo and run the following commands.
```
python3 setup.py build
python3 setup.py install
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
    with console:
        for i in range(23):
            console.print("    |" + " " * round(abs(sin((x + i) * 0.05)) * 9.5) + "O") # Prints to the custom console's buffer (works the same as python's built-in print)
    
    x += 1

    sleep(1/60)
```
![Demo GIF](https://media0.giphy.com/media/gXfAUJAD8hHwBcJIFP/giphy.gif?cid=790b7611aab0b776e0e3796d1e0e0e60f7012fc4300d0b9e&rid=giphy.gif&ct=g)

```python
with console:    
    console.print("Hello, world!")
    console.print("Another message!")

# is the same as

console.clear()

console.print("Hello, world!")
console.print("Another message!")

console.update()
```

# Downloads
[![Downloads](https://pepy.tech/badge/consoledraw)](https://pepy.tech/project/consoledraw) [![Downloads](https://pepy.tech/badge/consoledraw/month)](https://pepy.tech/project/consoledraw) [![Downloads](https://pepy.tech/badge/consoledraw/week)](https://pepy.tech/project/consoledraw)

# Supported Operating Systems
The consoledraw module should be supported on Windows, Linux and Mac (although it has not been tested on Mac).
