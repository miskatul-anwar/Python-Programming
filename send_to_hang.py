#! python3
import time 
import pyautogui
count = 5
n = int(input("How many Times? "))
prompt_to_show = input("Text to process: ")
print("Process Starting in...")
for i in range(5):
    print(count)
    time.sleep(1)
    count = count - 1
for i in range(n):
    pyautogui.typewrite(prompt_to_show)
    pyautogui.press("enter")
    time.sleep(0.5)
