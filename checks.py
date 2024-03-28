import pyautogui # type: ignore[import-untyped]
import time
time.sleep(2)
pr = pyautogui.displayMousePosition() 
print(pr)
# print(pyautogui.screenshot())
