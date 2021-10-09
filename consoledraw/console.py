import os

if os.name == 'nt':
    import ctypes
    import msvcrt

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

class Console:
    def __init__(self, hideCursor: bool = True) -> None:
        self.text = ""

        if hideCursor:
            if os.name == "nt":
                ci = _CursorInfo()
                handle = ctypes.windll.kernel32.GetStdHandle(-11)
                ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
                ci.visible = False
                ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
            elif os.name == "posix":
                print("\x1b[?25l")
        
        self.update()
    
    def write(self, text: str) -> None:
        self.text += text

    def print(self, *args, **kwargs) -> None:
        if "file" in kwargs:
            kwargs.pop("file")
        print(*args, **kwargs, file=self)
    
    def clear(self) -> None:
        self.lastText = self.text.rstrip()
        self.text = ""
        print(end="\033[0;0f")

    def update(self) -> None:
        self.text = self.text.rstrip()

        grid = []
        size = os.get_terminal_size()
        for _ in range(size.lines - 1):
            row = []
            for _ in range(size.columns):
                row.append(" ")
            grid.append(row)

        x, y = 0, 0
        for char in self.text:
            if char == "\n":
                x = 0
                y += 1
            else:
                grid[y][x] = char
                if (x := x + 1) == size.columns:
                    x = 0
                    y += 1

        print("".join(["".join(row) for row in grid]), end="")