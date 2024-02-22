from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import pyautogui
imLeave = pyautogui.screenshot(region=(-596,75,-45,1015))
imLeave = pyautogui.screenshot('new.png')