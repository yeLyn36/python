import pyautogui as pag
import time

if __name__ == "__main__":
    datas = pag.locateAllOnScreen("크롬.PNG")
    for data in datas:
        print(data)
        center = pag.center(data)
        pag.moveTo(center, duration=1)