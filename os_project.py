print ("mouse driver is loading .......")
import sys
from win32 import win32api
import win32con
import win32gui
import serial,time
import subprocess
import bluetooth
from bluetooth import discover_devices

ser = serial.Serial('com4',9600)
time.sleep(3)

ser.flushInput()

def lclick(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
def rclick(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)


"""if (len(sys.argv) < 4):
	print ("Usage: python mousemove.py dx dy speed")
	sys.exit()"""



print ("mouse driver is loaded...")
print(" details are")
print("0-0-0.......Mouse on ")
print("0-0-1.......Mouse off ")
print("0-1-0.......Wi-Fi Details ")
print("0-1-1.......Bluetooth Details ")
print("1-0-0.......Screen off ")
print("1-0-1.......Screen on ")

def mouse():
    current = win32api.GetCursorPos()
    cx = lead_x = int(current[0])
    cy = lead_y = int(current[1])
    last = time.time()

    while(True):
            if (ser.inWaiting()>0):
                    xx=ser.readline()
                    xx=int(xx.decode())
                    #print(xx)
                    if win32api.GetAsyncKeyState(ord('X')):
                            sys.exit()
                    elif xx == 77:
                            lead_x=lead_x+3
                    elif xx == 33:
                            lead_x=lead_x-3
                    elif xx == 88:
                            lead_y=lead_y-3
                    elif xx == 22:
                            lead_y=lead_y+3
                    elif xx == 66:
                            p=win32api.GetCursorPos()
                            lclick(p[0],p[1])
                    elif xx == 11:
                            p=win32api.GetCursorPos()
                            rclick(p[0],p[1])
                    elif xx == 1:
                            print("Cursor lost its control")
                            return()
                            #sys.exit()
                    
            win32api.SetCursorPos((lead_x,lead_y))
            time.sleep(0.001)
def blue():
    
    #--Pair HC-05 with PC first
    
    #target_name = "HC-05"
    #target_address = None
    print(" Bluetooth Details are Loading ....")
    nearby_devices = discover_devices()
    print (nearby_devices)
    for bdaddr in nearby_devices:
        print (bluetooth.lookup_name( bdaddr ))
def wi_fi():
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    print(ssids)

def s_off():
    print("Screen is off Now")
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND,
                       win32con.SC_MONITORPOWER, 2)
    return()
def s_on():
    print("Screen is on Now")
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND,
                       win32con.SC_MONITORPOWER, -1)

while(True):
            if (ser.inWaiting()>0):
                    x=ser.readline()
                    x=int(x.decode())
                    if x == 0:
                            print("Cursor is in control")
                            mouse()
                    elif x ==2:
                            wi_fi()
                    elif x== 3:
                            blue()
                    elif x == 4:
                            s_off()
                    elif x == 5:
                            s_on()


