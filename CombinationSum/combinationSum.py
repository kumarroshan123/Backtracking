from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(arr, ar, i, k, res):
            if k==0:
                res.append(ar.copy())
            for a in range(i, len(arr)):
                if k-arr[a]>=0:
                    ar.append(arr[a])
                    backtrack(arr, ar, a, k-arr[a], res)
                    ar.pop()

        res = []
        ar = []
        backtrack(candidates, ar, 0, target, res)
        return res