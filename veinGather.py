import pyautogui
import time
import win32api
from pytesseract import pytesseract 
from PIL import Image 

# 
# Go to Realm
# Check if already gathering
# If yes check how much time left
# Go to Map
# Go to Outer Realm
# Enter
# Check on vein
# if no vein Find empty spot leftclickdown and move
# check again
# nNo veins found, get back to realm
# If we find vein, click on it
#  click occupy or get how much time left and get back to
# click Ok
# check if we got tp back

# Global
path_img = 'timeleft.png'
path_img2 = 'asdas.png'
# Although download https://github.com/UB-Mannheim/tesseract/wiki
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Pictures
realm = 'realm'
gather = 'gathering'
gathering = 0

def click(task):
    try:
        xm,ym = pyautogui.locateCenterOnScreen(f"{task}.png", confidence=0.7)   
        pyautogui.click(xm, ym)
        print(f"Found {task}.png")
        time.sleep(1)
        return(1)  
    except pyautogui.ImageNotFoundException:
        print(f"Couldn't find {task}.png")
        return(0)

def checkGather(gather):
    try:
        f=pyautogui.locateOnScreen(f"{gather}.png", confidence=0.7)
        return f
    except pyautogui.ImageNotFoundException:
        return False


def time_left(img_path):
    img = Image.open(img_path) 
    pytesseract.tesseract_cmd = path_to_tesseract 
    text = pytesseract.image_to_string(img,config='--psm 6')
    print(text)
    time_string = text[:-1]
    print(time_string)
    # minutes = time_string[-5:-3]
    # seconds = time_string[-2:]
    # total = int(minutes)*60+int(seconds)
    # return total
 # Our main thread
    
"""
if(click(realm) == 1):
    coordinatesOfGather = checkGather(gather)
    if(coordinatesOfGather):
        gathering = 1
        pyautogui.doubleClick(coordinatesOfGather)
        print('Gathering')
    else:
        gathering = 0
        print('Not Gathering')

r = checkGather(gather)
pyautogui.click(r)
time.sleep(1)
pyautogui.mouseDown(r)
time.sleep(0.1)
pyautogui.mouseUp(r)
# 
"""
# im = pyautogui.screenshot('timeLeft.png',region=(1550,639, 120, 30))
time.sleep(1)
our_time = time_left(path_img)



