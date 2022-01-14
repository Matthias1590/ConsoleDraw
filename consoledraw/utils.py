import os


if os.name == "nt":  # Windows
    import ctypes

    __console_handle = ctypes.windll.kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

    def set_cursor_visibility(visible: bool) -> None:
        ci = _CursorInfo()
        ctypes.windll.kernel32.GetConsoleCursorInfo(__console_handle, ctypes.byref(ci))
        ci.visible = visible
        ctypes.windll.kernel32.SetConsoleCursorInfo(__console_handle, ctypes.byref(ci))

    def clear_screen() -> None:
        os.system("cls")

    def set_cursor_position(x: int, y: int) -> None:
        value = x + (y << 16)
        ctypes.windll.kernel32.SetConsoleCursorPosition(__console_handle, value)


else:  # Linux and macOS

    def set_cursor_visibility(visible: bool) -> None:
        print("\x1b[?25h" if visible else "\x1b[?25l")

    def clear_screen() -> None:
        print("\x1b[2J\x1b[H")

    def set_cursor_position(x: int, y: int) -> None:
        print(end=f"\033[{x};{y}f")
