from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        pivot_index = -1
        total_sum = sum(nums)
        right = 0
        indices = []
        for i in reversed(range(len(nums))):
            if right == total_sum - (nums[i] + right):
                indices.append(i)
            right += nums[i]
        print(indices)
        return pivot_index if len(indices) == 0 else indices.pop()


print(Solution().pivotIndex([-1,-1,0,0,-1,-1]))
