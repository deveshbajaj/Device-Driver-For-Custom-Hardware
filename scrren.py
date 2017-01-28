"""import win32gui
import win32con
import time

off
win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND,
                       win32con.SC_MONITORPOWER, 2)

time.sleep(10)
#on
win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND,
                       win32con.SC_MONITORPOWER, -1)

"""
# sleep
"""win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND,
                       win32con.SC_MONITORPOWER, 1)"""
import os
os.system('rundll32.exe powrprof.dll,SetSuspendState 1,1,0')
