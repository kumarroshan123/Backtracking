from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def safe(arr, row, col, n):
            for i in range(n):
                if arr[row][i] == "Q":
                    return False
            for i in range(n):
                if arr[i][col] == "Q":
                    return False
            r, c = row, col
            while r < n and c < n:
                if arr[r][c] == "Q":
                    return False
                r += 1
                c += 1
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if arr[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if arr[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            r, c = row + 1, col - 1
            while r < n and c >= 0:
                if arr[r][c] == "Q":
                    return False
                r += 1
                c -= 1
            return True
        
        def q(arr, row, n, result):
            if row == n:
                result.append(["".join(row) for row in arr])
                return
            for i in range(n):
                if safe(arr, row, i, n):
                    arr[row][i] = "Q"
                    q(arr, row + 1, n, result)
                    arr[row][i] = "."
                    
        arr = [["."] * n for _ in range(n)]
        result = []
        q(arr, 0, n, result)
        return result