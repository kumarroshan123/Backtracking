class Solution:
    def totalNQueens(self, n: int) -> int:
        def safe(arr, row, col, n):
            for i in range(n):
                if arr[row][i] == 1:
                    return False
            for i in range(n):
                if arr[i][col] == 1:
                    return False
            r = row
            c = col
            while (r < n and c < n):
                if arr[r][c] == 1:
                    return False
                r = r + 1
                c = c + 1
            r = row - 1
            c = col - 1
            while (r >= 0 and c >= 0):
                if arr[r][c] == 1:
                    return False
                r = r - 1
                c = c - 1
            r = row - 1
            c = col + 1
            while (r >= 0 and c < n):
                if arr[r][c] == 1:
                    return False
                r = r - 1
                c = c + 1
            r = row + 1
            c = col - 1
            while (r < n and c >= 0):
                if arr[r][c] == 1:
                    return False
                r = r + 1
                c = c - 1
            return True

        def solve(arr, row, c, n):
            if row == n:
                c[0] += 1
                return
            for i in range(n):
                if safe(arr, row, i, n):
                    arr[row][i] = 1
                    solve(arr, row + 1, c, n)
                    arr[row][i] = 0

        arr = [[0] * n for _ in range(n)]
        c = [0]
        solve(arr, 0, c, n)
        return c[0]