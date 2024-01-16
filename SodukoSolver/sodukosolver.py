class Solution:
    def check(self, board: List[List[str]], row: int, col: int, k: int) -> bool:
        return (
            str(k) not in board[row] and
            str(k) not in [board[i][col] for i in range(9)] and
            str(k) not in [board[i][j] for i in range(3 * (row // 3), 3 * (row // 3) + 3) for j in range(3 * (col // 3), 3 * (col // 3) + 3)]
        )

    def fill(self, board: List[List[str]], row: int, col: int) -> bool:
        if row == 9:
            return True
        if col == 9:
            return self.fill(board, row + 1, 0)
        if board[row][col] == ".":
            for i in range(1, 10):
                if self.check(board, row, col, i):
                    board[row][col] = str(i)
                    if self.fill(board, row, col + 1):
                        return True
                    else:
                        board[row][col] = "."
            return False
        return self.fill(board, row, col + 1)

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.fill(board, 0, 0)