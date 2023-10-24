from time import sleep
import keyboard
import pyautogui

# Positions of the tree based on character position
# right = tree is on the right of character ...
right = (1264,426,80,80)
left = (1198,425,80,80)
top = (1231,393,80,80)
bot = (1231,458,80,80)

# Static positions
AXE = (1546, 551)
MANA = (1880, 235, 35, 22)
FOOD = (1583, 549)
MINIMAP = (1728, 31, 183, 182)

list_positions = [right, left, top, bot]

# Move mouse to center of the tree
def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

# Use axe on tree -> gather sticks, dried sticks, etc
def get_tree(location):
  if location != None:
    sleep(0.5)
    pyautogui.moveTo(AXE)
    pyautogui.click(AXE, button='right')
    sleep(0.5)
    move(location)
    pyautogui.click(button='left')
    sleep(1)

# Click on minimap
def move_and_click(location):
  move(location)
  pyautogui.click()

# Conjure rune (cast spell saved on F3 hotkey)
def conjure_rune():
  mana = pyautogui.locateOnScreen('images/mana.PNG', confidence=0.7, region=MANA)
  if mana != None:
    keyboard.press_and_release('F3')

# Eat food (right slot of the small axe)
def eat_food():
  pyautogui.moveTo(FOOD)
  pyautogui.click(FOOD, button='right')

# Initially the loop is OFF
loop_ativo = False

def iniciar_loop():
    global loop_ativo
    loop_ativo = True

def pausar_loop():
    global loop_ativo
    loop_ativo = False

# Press P in-game to start running
keyboard.add_hotkey('p', iniciar_loop)
# Press K in-game to pause
keyboard.add_hotkey('k', pausar_loop)

tree_counter = 0

while True:
  if loop_ativo:
    for index in range(61):
      while True:
        position_in_map = pyautogui.locateOnScreen('icons/icon_{}.png'.format(index), confidence=0.90, region=MINIMAP)
        print('waypoint: {}'.format(index))
        if position_in_map != None:
          move_and_click(position_in_map)
          sleep(6)
          conjure_rune()
          eat_food()
          sleep(0.5)
          print('Harvested trees: {}'.format(tree_counter))
          check_position = pyautogui.locateOnScreen('icons/icon_{}.png'.format(index), confidence=0.90, region=MINIMAP)
          if check_position == None:
            tree_counter += 1
            for position in list_positions:
              for index in range(8):
                while True:
                  tree = pyautogui.locateOnScreen('trees/tree_{}.PNG'.format(index), confidence=0.7, region=position)
                  if tree != None:
                    get_tree(tree)
                  else:
                    break
            break
