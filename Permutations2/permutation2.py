from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def p(ar, l, r, temp):
            if l == r:
                temp.append(ar[:]) 
            for i in range(l, r):
                ar[l], ar[i] = ar[i], ar[l]
                p(ar, l + 1, r, temp)
                ar[l], ar[i] = ar[i], ar[l]

        n = len(nums)
        temp = []
        p(nums, 0, n, temp)
        temp.sort()
        i=0
        while(i<len(temp)-1):
            if temp[i]==temp[i+1]:
                temp.remove(temp[i])
            else:
                i=i+1
        return temp