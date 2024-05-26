from win32gui import FindWindow, PostMessage
import win32.lib.win32con as win32con


class WindowNotFound(Exception):
    ...


def find_window_by_name(window_name: str, class_name=None) -> int:
    """find a window by its class_name"""
    handle = FindWindow(class_name, window_name)
    if handle == 0:
        raise WindowNotFound(f"'{window_name}'")
    return handle


def close_window(handle: int):
    PostMessage(handle, win32con.WM_CLOSE, 0, 0)


handle = find_window_by_name("@kevin - Discord")
close_window(handle)
