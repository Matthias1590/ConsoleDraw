import os
from copy import deepcopy
from typing import List

if os.name == "nt":
    import ctypes
    import msvcrt

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

    def setCursorVisibility(visible: bool) -> None:
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(
            handle, ctypes.byref(ci))
        ci.visible = visible
        ctypes.windll.kernel32.SetConsoleCursorInfo(
                handle, ctypes.byref(ci))
else:
    def setCursorVisibility(visible: bool) -> None:
        print("\x1b[?25h" if visible else "\x1b[?25l")


class Console:
    def __init__(self, hideCursor: bool = True) -> None:
        self.text = ""
        self.__gridCache = {}

        if hideCursor:
            setCursorVisibility(False)

        self.update()

    def __enter__(self, *args, **kwargs) -> None:
        self.clear()

    def __exit__(self, *args, **kwargs) -> None:
        self.update()

    def __generateGrid(self) -> List[List[str]]:
        # If we have already generated a grid with the current size of the terminal, just return a copy of that instead of generating it again
        size = os.get_terminal_size()
        if size in self.__gridCache:
            return deepcopy(self.__gridCache[size])

        # Generate a grid the size of the terminal
        grid = []
        for _ in range(size.lines - 1):
            row = []
            for _ in range(size.columns):
                row.append(" ")
            grid.append(row)

        # Cache the grid so we don't have to generate it again later
        self.__gridCache[size] = grid

        return deepcopy(grid)

    def write(self, text: str) -> None:
        "Writes to the console (use Console.print if you want this to behave like python's built-in print function)."

        self.text += text

    def print(self, *args, **kwargs) -> None:
        "Prints to the console (behaves like python's built-in print function)."

        # Make sure to remove the file keyword argument if it exists, because we already set it ourselves
        if "file" in kwargs:
            kwargs.pop("file")
        print(*args, **kwargs, file=self)

    def clear(self) -> None:
        "Clears the console's buffer."

        self.lastText = self.text.rstrip()
        self.text = ""
        print(end="\033[0;0f")

    def update(self) -> None:
        "Prints the console's buffer to the actual console."

        self.text = self.text.rstrip()

        grid = self.__generateGrid()

        x, y = 0, 0
        maxX = len(grid[0]) - 1
        maxY = len(grid) - 1
        for char in self.text:
            if char == "\n":
                x = 0
                y += 1
            else:
                if y > maxY or x > maxX:
                    raise ValueError(
                        "The console is too small to display the buffer.")
                grid[y][x] = char
                if x == maxX:
                    x = 0
                    y += 1
                else:
                    x += 1

        print(end="".join(["".join(row) for row in grid]))
