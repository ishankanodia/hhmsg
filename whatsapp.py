import pyautogui
import time
time.sleep(3)

count=0
while count<=25:
    pyautogui.typewrite(f"Hello {count}")
    pyautogui.press("enter")
    count-=1