from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def f(p, k, s, c,ind, ar, ans):
            if k == c:
                ans.append(ar[:]) 
            if  k <= c:
                return
            for i in range(ind , p+1):
                ar.append(i)
                f(p, k, s + i, c + 1, i+1 , ar, ans)
                ar.pop()

        ar = []
        ans = []
        f(n, k, 0, 0,1, ar, ans)
        return ans