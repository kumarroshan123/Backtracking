class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def sq(t, s, e, a, result):
            if s <= e:
                b=t[:]
                b.sort()
                if b[:] not in result:
                    result.append(b[:])
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