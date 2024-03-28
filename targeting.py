import pyautogui # type: ignore[import-untyped]
import time
import random


found = 0
def look(target):
    try:
        xm,ym = pyautogui.locateCenterOnScreen(f"{target}.png", confidence=0.6)
        return xm, ym
    except pyautogui.ImageNotFoundException:
            print(f"Couldn't find {target}.png")
            return 0

def lookFor():
    coord = look('fight')
    print(coord)
    if(coord != 0):
         xm, ym = coord
         pyautogui.moveTo(xm-150,ym-200)
         r = random.randint(100,300)
         randomValue = random.randint(0,2)
         multiplier = 1 if randomValue else -1
         pyautogui.drag(multiplier * r, 0, 1, button='left')
         result = look('target')
         if(result):
              return result
         else:
              return 0
# pyautogui.click(look('map'))
        #  main

while(True):
    coords = look('map')
    if(coords != 0 ):
        pyautogui.click(look('map'))
        while(look('target') == 0):         
            lookFor()
            time.sleep(0.2)
        pyautogui.click(look('target'))
        pyautogui.click(look('fight'))
        time.sleep(15 + random.randint(0,18)*0.3)
    time.sleep(1)

