from time import sleep
import pyautogui

right = (1264,426,80,80)
left = (1198,425,80,80)
top = (1231,393,80,80)
bot = (1231,458,80,80)

axe = (1546, 551)
mana = (1880, 235)

list_positions = [right, left, top, bot]

# TODO: Fix trees caption (function get_tree()) 
# Some trees is just been captured in certain angles
# (e.g. large pines are beeing captured only if the character is on their north-west tile) 

#'''
while True:
    tree_right = pyautogui.locateOnScreen('trees/tree_0.png', confidence=0.7, region = right)
    tree_left = pyautogui.locateOnScreen('trees/tree_0.png', confidence=0.7, region = left)
    tree_top = pyautogui.locateOnScreen('trees/tree_0.png', confidence=0.7, region = top)
    tree_bot = pyautogui.locateOnScreen('trees/tree_0.png', confidence=0.7, region = bot)
    tree_bot = pyautogui.locateOnScreen('trees/tree_0.png', confidence=0.7, region = bot)
    mana = pyautogui.locateOnScreen('images/mana.PNG', confidence=0.7)
    minimap = pyautogui.locateOnScreen('images/minimap.PNG', confidence=0.7)
    #print('tree right = {}'.format(tree_right))
    #print('tree left = {}'.format(tree_left))
    #print('tree top = {}'.format(tree_top))
    #print('tree bot = {}'.format(tree_bot))
    #print(mana)
    print(minimap)
    #tree = pyautogui.locateOnScreen('images/tree_5.PNG', confidence=0.7)
    #print(tree)
    print(pyautogui.position())
#'''

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
      
# While loop to gather trees controlling the character manually
# This loop automatically gather trees in the list_positions spots (right, left, top and bottom of the character)
#while True:
#    for position in list_positions:
#      for index in range(8):
#        tree = pyautogui.locateOnScreen('images/tree_{}.PNG'.format(index), confidence=0.7, region=position)
#        get_tree(tree)
#        #break
