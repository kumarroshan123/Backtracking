from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate_permutations(nums, left, right, temp):
            if left == right:
                temp.append(nums.copy())
            for i in range(left, right):
                nums[left], nums[i] = nums[i], nums[left]
                generate_permutations(nums, left + 1, right, temp)
                nums[left], nums[i] = nums[i], nums[left]
        
        n = len(nums)
        temp = []
        generate_permutations(nums, 0, n, temp)
        return temp