import os
import time
import subprocess

import shutil
from pathlib import Path

ADB = "adb"  # or full path to adb if needed
DEVICE = "127.0.0.1:5555"  # BlueStacks default

# --- Connect to BlueStacks ---
def adb(cmd):
    full_cmd = f"{ADB} -s {DEVICE} {cmd}"
    print(f"Running: {full_cmd}")
    return subprocess.run(full_cmd, shell=True, capture_output=True)

def trigger_media_scan(filename="image.png"):
    adb_cmd = f'adb -s 127.0.0.1:5555 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/{filename}'
    subprocess.run(adb_cmd, shell=True)
    print(f"📷 Triggered media scan for: {filename}")
    
def connect_bluestacks():
    subprocess.run(f"{ADB} connect {DEVICE}", shell=True)

def push_image(image_path):
    adb(f"push {image_path} /sdcard/Pictures/")

def launch_twitch():
    adb("shell monkey -p com.zhiliaoapp.musically -c android.intent.category.LAUNCHER 1")

def tap(x, y):
    adb(f"shell input tap {x} {y}")

def swipe(x1, y1, x2, y2):
    adb(f"shell input swipe {x1} {y1} {x2} {y2}")

def set_vertical():
    adb("shell settings put system user_rotation 1")

# --- Main Sequence ---
connect_bluestacks()
time.sleep(2)


push_image("story.png")
trigger_media_scan("story.png")
time.sleep(1)

set_vertical()

launch_twitch()
time.sleep(6)  # wait for app to load



# Open story UI
tap(975, 1885)  # click on your profile on the bottom right
time.sleep(6)
tap(595, 280)  # click on the + icon on your profile picture
time.sleep(5)
tap(120, 600)  # click last image
time.sleep(4)
tap(1050, 420)  # click on sound note to disable music which gets automatically added
time.sleep(4)
tap(1025, 1845)  # click the delete pastebin icon on the bottom right to remove the sound
time.sleep(4)
tap(42, 72)  # close sound overlay
time.sleep(4)
tap(570, 1878)  # confirm post story button

# Done
print("✅ Done (check your Twitch app manually)")
