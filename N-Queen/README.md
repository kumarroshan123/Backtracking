# N-Queen
(https://leetcode.com/problems/n-queens/description/)
<sup>

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:

<img alt="error" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg">
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above


Example 2:

Input: n = 1
Output: [["Q"]]


 

Constraints:

1 <= n <= 9

</sup>
```
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
```