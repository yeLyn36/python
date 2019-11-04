class TicTacTo:
    def __init__(self):
        self.board = [[".",".","."],
                      [".",".","."],
                      [".",".","."]]
        self.current_turn = "x"

    def set(self, row, col):
        # if self.current_turn == 'o':
        #     self.current_turn = 'x'
        # else :
        #     self.current_turn = 'o'
        if self.get(row, col) == ".":
            self.current_turn = 'x' if self.current_turn == 'o' else 'o'
            self.board[row][col] = self.current_turn

    def get(self, row, col):
        return self.board[row][col]

    def check_winner(self):
        check = self.current_turn
        for i in range(3):
            if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == check:
                # 세로
                return check
            if self.get(0, i) == self.get(1, i) == self.get(i, 2) == check:
                # 가로
                return check
        if self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == check:
            # 대각선 \
            return check
        if self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check:
        # 대각선 /
            return check

        if not "." in self.board:
            return "d" # draw

    def __str__(self):
        s = ""
        for i, v in enumerate(self.board):
            for j, a in enumerate(self.board):
                s += str(v[j])
                if j % 3 == 2:
                    s += "\n"
        return s

