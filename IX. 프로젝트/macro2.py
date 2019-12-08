import pyautogui as pag
import time     #sleep

if __name__ == '__main__':
    pag.moveTo(200, 200, 2)
    pag.click()
    pag.typewrite("I will fall a sleep", interval=0.3)
    pag.press("enter")
    pag.typewrite("it's too sleepy")
    pag.press("hangul")
    pag.typewrite("dl wjdehaus wkrp gownjdiwl")
    pag.press("hangul")