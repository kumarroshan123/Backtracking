from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(arr, ar, i, k, res):
            if k==0:
                res.append(ar.copy())
            if k<0 or i>=len(arr):
                return
            for a in range(i, len(arr)):
                if a > i and arr[a] == arr[a-1]:
                    continue
                ar.append(arr[a])
                backtrack(arr, ar, a+1, k-arr[a], res)
                ar.pop()
        candidates.sort()
        res = []
        ar = []
        backtrack(candidates, ar, 0, target, res)
        return res
