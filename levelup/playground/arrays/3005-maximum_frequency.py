import collections

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        count = collections.Counter(nums)
        maxFreq = max(count.values())
        return sum(freq == maxFreq for freq in count.values()) * maxFreq

print(Solution().maxFrequencyElements([1,2,2,3,4]))
