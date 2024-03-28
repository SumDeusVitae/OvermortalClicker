import pyautogui
import time

suggestion = 0
while(True):
    try:
        xm,ym = pyautogui.locateCenterOnScreen("suggestion.png", confidence=0.9)
        pyautogui.click(x=xm+50,y=ym, clicks=2, interval=1)
        print(f"Found suggestion Coords:{xm,ym}")
        suggestion = 1
    except pyautogui.ImageNotFoundException:
        print(f"Couldn't find suggestion")
    time.sleep(1)
    if(suggestion):
        try:
            xm,ym = pyautogui.locateCenterOnScreen("accept.png", confidence=0.8)
            pyautogui.click(xm, ym)
            print(f"Found accept Coords:{xm,ym}")  
            suggestion = 0
        except pyautogui.ImageNotFoundException:
            print(f"Couldn't find accept")
        time.sleep(1)
    