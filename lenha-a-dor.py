from time import sleep
import keyboard
import pyautogui

# Positions of the tree based on character position
# right = tree is on the right of character ...
right = (1264,426,80,80)
left = (1198,425,80,80)
top = (1231,393,80,80)
bot = (1231,458,80,80)

# Static small axe position
axe = (1546, 551)

list_positions = [right, left, top, bot]

# Move mouse to center of the tree
def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

# Use axe on tree -> gather sticks, dried sticks, etc
def get_tree(location):
  if location != None:
    sleep(0.5)
    pyautogui.moveTo(axe)
    pyautogui.click(axe, button='right')
    sleep(0.5)
    move(location)
    pyautogui.click(button='left')
    sleep(1)

# Click on minimap
def move_and_click(location):
  move(location)
  pyautogui.click()

# Press P in-game to start running
keyboard.wait('p')

# TODO: check if the tree was gathered, it have a chance to fail. 
# If fails -> call get_tree(tree) until the tree be completely gathered
for index in range(17):
  while True:
    position_in_map = pyautogui.locateOnScreen('icons/icon_{}.png'.format(index), confidence=0.90)
    print(position_in_map)
    if position_in_map != None:
      move_and_click(position_in_map)
      sleep(3)
      check_position = pyautogui.locateOnScreen('icons/icon_{}.png'.format(index), confidence=0.90)
      if check_position == None:
        for position in list_positions:
          for index in range(8):
            tree = pyautogui.locateOnScreen('images/tree_{}.PNG'.format(index), confidence=0.7, region=position)
            get_tree(tree)
        #break
