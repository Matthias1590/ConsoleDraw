import os


if os.name == "nt":
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

    def set_cursor_visibility(visible: bool) -> None:
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = visible
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))


else:

    def set_cursor_visibility(visible: bool) -> None:
        print("\x1b[?25h" if visible else "\x1b[?25l")