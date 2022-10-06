import time
import pynput
import pyperclip
from pynput.mouse import Button
from pynput.keyboard import Key

mouse=pynput.mouse.Controller()
keyboard=pynput.keyboard.Controller()
words=open('dictionary.txt').readlines()
clipboard=''

def cycle(key):
    if str(key)=='Key.esc': listener.stop()
    if str(key)!="Key.ctrl_r": return
    mouse.click(Button.left)
    time.sleep(.1)
    mouse.click(Button.left)
    keyboard.press(Key.ctrl)
    keyboard.tap('c')
    keyboard.release(Key.ctrl)
    global clipboard
    while clipboard==pyperclip.paste(): continue
    clipboard=pyperclip.paste()
    mouse.move(0,-50)
    mouse.click(Button.left)
    mouse.move(0,50)
    for word in words:
        if clipboard in word.lower():
            keyboard.type(word.lower())
            keyboard.tap(Key.enter)
            words.remove(word)
            break

listener=pynput.keyboard.Listener(on_press=cycle,supress=True)
listener.start()
listener.join()
