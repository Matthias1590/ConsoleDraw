import os

from copy import deepcopy
from typing import Dict, List

from .errors import ConsoleSizeError
import consoledraw.utils as utils


class Console:
    def __init__(self, hide_cursor: bool = True, clear_screen: bool = True) -> None:
        self.__text: str = ""
        self.__grid_cache: Dict[os.terminal_size, List[List[str]]] = {}

        utils.set_cursor_visibility(not hide_cursor)
        if clear_screen:
            utils.clear_screen()

        self.update()

    def __enter__(self, *args, **kwargs) -> None:
        self.clear()

    def __exit__(self, *args, **kwargs) -> None:
        self.update()

    def __generate_grid(self) -> List[List[str]]:
        "Generates the grid for the console."

        # If we have already generated a grid with the current size of the terminal, just return a copy of that instead of generating it again
        size = os.get_terminal_size()
        if size in self.__grid_cache:
            return deepcopy(self.__grid_cache[size])

        # Generate a grid the size of the terminal
        grid = []
        for _ in range(size.lines - 1):
            row = []
            for _ in range(size.columns):
                row.append(" ")
            grid.append(row)

        # Cache the grid so we don't have to generate it again later
        self.__grid_cache[size] = grid

        return deepcopy(grid)

    def write(self, text: str) -> None:
        "Writes to the console (use Console.print if you want this to behave like Python's built-in print function)."

        self.__text += text

    def print(self, *args, **kwargs) -> None:
        "Prints to the console (behaves like Python's built-in print function)."

        # Make sure to remove the file keyword argument if it exists, because we already set it ourselves
        if "file" in kwargs:
            kwargs.pop("file")
        print(*args, **kwargs, file=self)

    def clear(self) -> None:
        "Clears the console's buffer."

        self.__text = ""
        utils.set_cursor_position(0, 0)

    def update(self) -> None:
        "Prints the console's buffer to the actual console."

        self.__text = self.__text.rstrip()

        grid = self.__generate_grid()

        x, y = 0, 0
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1
        for char in self.__text:
            if char == "\n":
                x = 0
                y += 1
            else:
                if y > max_y or x > max_x:
                    raise ConsoleSizeError(
                        "The console is too small to display the buffer"
                    )
                grid[y][x] = char
                if x == max_x:
                    x = 0
                    y += 1
                else:
                    x += 1

        print(end="".join(["".join(row) for row in grid]))
