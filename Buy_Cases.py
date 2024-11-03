import pyautogui
import keyboard
import threading

start_coords = [1063, 253]
buy_coords = [800, 891]
offset = 74
items_count = 8

def main():
    for i in range(items_count):
        if(not running): break
        for j in range(items_count):
            if(not running): break
            pyautogui.moveTo(start_coords[0] + offset * j, start_coords[1] + offset * i, _pause = 0.01)
            keyboard.press('shift')
            pyautogui.click()
            keyboard.release('shift')
            pyautogui.moveTo(buy_coords[0], buy_coords[1], _pause = 0.01)
            pyautogui.click()

def key_listener():
    global running
    keyboard.wait('f5') 
    running = False

if __name__ == "__main__":
    running = True

    key_thread = threading.Thread(target=key_listener)
    key_thread.start()

    main()

    key_thread.join()