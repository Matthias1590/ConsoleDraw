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
example.py:
```python
from consoledraw import Console
from datetime import datetime
from time import sleep

console = Console()

format = """
    ╔══════════╗
    ║ {} ║
    ╚══════════╝
"""

while True:
    with console:
        console.print(format.format(datetime.strftime(datetime.now(), "%H:%M:%S")))

    sleep(0.5)
```
![Demo GIF](https://i.giphy.com/media/J5EEMFnL8K1oTneliV/giphy.webp)

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
