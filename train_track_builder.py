import time

import pyautogui
import keyboard

while True:
    if keyboard.is_pressed('q'):
        x, y = pyautogui.position()
        pyautogui.mouseDown()
        off_x = 10
        off_y = 10
        drill_key = '2'
        rail_key = '4'
        block_key = '3'

        move_fwd = True

        while True:
            pyautogui.moveTo(x, y + off_x, 0.3)
            pyautogui.moveTo(x, y - off_y, 0.3)

            # PLACE BLOCK
            #pyautogui.press(block_key)
            #pyautogui.leftClick()

            if keyboard.is_pressed('s'):
                move_fwd = False

            if keyboard.is_pressed('s') and move_fwd == False:
                move_fwd = True

            if move_fwd:
                pyautogui.keyDown('d')
                time.sleep(0.1)
                pyautogui.keyUp('d')

            if keyboard.is_pressed('w'):
                #DRILL
                off_x = off_x + 5
                off_y = off_y + 5

                continue

            if keyboard.is_pressed('q'):
                print('X_off: ' + str(off_x))
                print('Y_off: ' + str(off_y))
                exit()