from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sq(t, s, e, a, result):
            if s <= e:
                result.append(t[:])
            for i in range(s, e):
                t.append(a[i])
                sq(t, i + 1, e, a, result)
                t.pop()

        n = len(nums)
        a = nums
        t = []
        result = []
        sq(t, 0, n, a, result)
        return result
