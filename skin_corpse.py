import pyautogui
import keyboard
from time import sleep

def skin_corpse():
    mouse_position = pyautogui.position()
    sleep(0.1)
    pyautogui.moveTo(1542, 549)
    sleep(0.1)
    pyautogui.click(button='right')
    sleep(0.1)
    pyautogui.moveTo(mouse_position.x, mouse_position.y)
    sleep(0.1)
    pyautogui.click(button='left')

keyboard.add_hotkey('F1', skin_corpse)

# Pause program
keyboard.wait("esc") 