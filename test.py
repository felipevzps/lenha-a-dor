from time import sleep
import pyautogui

right = (1264,426,80,80)
left = (1198,425,80,80)
top = (1231,393,80,80)
bot = (1231,458,80,80)

axe = (1546, 551)

list_positions = [right, left, top, bot]

'''
while True:
    tree_right = pyautogui.locateOnScreen('trees_test/tree_0.png', confidence=0.7, region = right)
    tree_left = pyautogui.locateOnScreen('trees_test/tree_0.png', confidence=0.7, region = left)
    tree_top = pyautogui.locateOnScreen('trees_test/tree_0.png', confidence=0.7, region = top)
    tree_bot = pyautogui.locateOnScreen('trees_test/tree_0.png', confidence=0.7, region = bot)
    print('tree right = {}'.format(tree_right))
    print('tree left = {}'.format(tree_left))
    print('tree top = {}'.format(tree_top))
    print('tree bot = {}'.format(tree_bot))
    #tree = pyautogui.locateOnScreen('images/tree_5.PNG', confidence=0.7)
    #print(tree)
    #print(pyautogui.position())
'''

def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

def get_tree(location):
  if location != None:
    sleep(0.5)
    pyautogui.moveTo(axe)
    pyautogui.click(axe, button='right')
    sleep(0.5)
    move(location)
    pyautogui.click(button='left')

while True:
    for position in list_positions:
      for index in range(8):
        tree = pyautogui.locateOnScreen('images/tree_{}.PNG'.format(index), confidence=0.7, region=position)
        get_tree(tree)
        #break