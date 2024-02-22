import pyautogui
import time

#Global
counter = 0

#function find and click
def findnClick(task):
    try:
        xm,ym = pyautogui.locateCenterOnScreen(f"{task}.png", confidence=0.7)
        fw = pyautogui.getActiveWindow()
        pyautogui.mouseUp()
        lastx, lasty = pyautogui.position()
        pyautogui.click(xm, ym)
        print(f"Found {task}.png")
        fw.activate()
        pyautogui.moveTo(lastx, lasty)
        if(task == challange):
            time.sleep(10)
            counter = 1
        else:
            time.sleep(1)
            counter = 0    
    except pyautogui.ImageNotFoundException:
        print(f"Couldn't find {task}.png")

# Our file names
challange = 'chalNew'
back = 'leaveNew'
confirm = 'confirm'
skip = 'nextStage'

# Our demon
while(True):
    if(counter == 0):
        findnClick(challange)
    findnClick(back)
    findnClick(confirm)
    # findnClick(skip)
    time.sleep(1)

#Scenario

# 1 Check if we have challange
# 2 I
