# SODUKO SOLVER
<sup>

This program is designed to solve a Sudoku puzzle by filling in the empty cells. A Sudoku solution must satisfy three rules:
1. Each digit 1-9 must occur exactly once in each row.
2. Each digit 1-9 must occur exactly once in each column.
3. Each digit 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The `.` character represents an empty cell.

Example
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Explanation: The input board is shown above and the only valid solution is shown below:

<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png">

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
</sup>

```

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

```
