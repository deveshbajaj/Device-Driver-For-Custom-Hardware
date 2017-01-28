





import win32con    
win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0)










"""import subprocess
results = subprocess.check_output(["netsh", "wlan", "show", "network"])
#print(results)
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
"""
