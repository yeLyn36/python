import pyautogui as pag
import time

if __name__ == "__main__":
    data = pag.locateOnScreen("크롬.PNG")
    print(data)

    # center = (data.left+(data.width/2), data.top+(data.height/2))
    center = pag.center(data)
    pag.moveTo(center, duration=2)
    pag.doubleClick()
