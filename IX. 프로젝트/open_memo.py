import pyautogui as pag
import time
if __name__ == '__main__':
    pag.click(5, 1053)
    pag.sleep(1)
    pag.typewrite("memo")
    pag.press("enter")
    pag.sleep(1)
    pag.typewrite("hello world")
    pag.press("enter")
    pag.press("enter")
    pag.press('hangul')
    pag.typewrite("qksrkqrnsk tptkddk")
    pag.hotkey('ctrl', 's')
    pag.typewrite("vkdlTjsdnjfem")
    pag.press("enter")

# 메모장 프로그램 실행 및 hello world 치고 enter 2번, 반갑구나 세상아 치고 저장 (파이썬월드.txt)

