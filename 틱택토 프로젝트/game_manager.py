from tictacto import TicTacTo

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

if __name__ == '__main__':
    gm = GameManager()
    gm.play()