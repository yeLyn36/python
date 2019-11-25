from tictacto import TicTacTo
import tkinter
from tkinter import messagebox
import math

class GameManager:
    def __init__(self):
        self.ttt = TicTacTo()

    def play(self):
        while True:
            # 보드판 보여주기
            print(self.ttt)
            # row, col 입력
            row = int(input("row : "))
            col = int(input("col : "))
            self.ttt.set(row, col)
            # 승자 확인
            if self.ttt.check_winner() == "O":
                print("O winner")
            elif self.ttt.check_winner() == "X":
                print("X winner")
            else :
                print("Draw, Great")
            pass

class GameManager_gui:
    def __init__(self):
        self.ttt = TicTacTo()
        CANVAS_SIZE = 300
        self.TILE_SIZE = CANVAS_SIZE / 3

        self.root = tkinter.Tk()
        self.root.title("틱택토")
        self.root.geometry(str(CANVAS_SIZE) + "x" + str(CANVAS_SIZE))
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg='white', width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()

    def play(self):
        self.root.mainloop()

if __name__ == '__main__':
    gm = GameManager_gui()
    gm.play()