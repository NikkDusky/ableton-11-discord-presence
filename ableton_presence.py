from pypresence import Presence
import random
import ctypes
import time
import os

os.system("title Ableton Live 11 Sutie - Discord Presence")

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

application_id = 858730122290003988

title = ""
program = None
project = None

btns = [
    {
        "label": "Live 11 Suite",
        "url": "https://www.ableton.com/en/shop/live/"
    },
        ]

RPC = Presence(application_id)
RPC.connect()
start_time = time.time()

while True:
    tmp = os.popen("tasklist").read()
    if "Ableton Live 11 Suite" in tmp:
        os.system("cls")
        print("Ableton Live 11 Suite is running...")
        def foreach_window(hwnd, lParam):
            global title
            if IsWindowVisible(hwnd):
                length = GetWindowTextLength(hwnd)
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                
                if buff.value[-21:] == "Ableton Live 11 Suite":
                    title = buff.value
                    
            return True
            
        EnumWindows(EnumWindowsProc(foreach_window), 0)

        title = title.split("-")
        try:
            program = (title[1])[1:]
            project = (title[0])[:-1]
        except IndexError:
            print("Index Error Catched...")
      
        print(f"Ableton: {program}")
        print(f"Project: {project}")

        RPC.update(
            state=f"{project}",
            details="Project",
            buttons=btns,
            large_image="icon",
            start=start_time
            )
    else:
        os.system("cls")
        print("Ableton Live 11 Suite not found...\nPlease, launch Ableton Live 11 Suite...")
    time.sleep(10)