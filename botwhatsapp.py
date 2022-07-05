from unittest import addModuleCleanup
import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+56996381318')
sleep(2)

with open ("spam.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
















