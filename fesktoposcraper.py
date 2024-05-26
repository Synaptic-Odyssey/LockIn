from pywinauto import Desktop
import pywinauto
windows = Desktop(backend="uia").windows()
print([w.window_text() for w in windows])
print(windows)

# dlg_spec = pywinauto.findwindows.find_window("@kevin - Discord")
# dlg_spec.minimize()