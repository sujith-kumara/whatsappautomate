import pyautogui
import time
time.sleep(4)
count = 0
while count<=100:
    pyautogui.typewrite("😘 All the best 😘")
    pyautogui.press("enter")
    time.sleep(1)
    

    count += 1