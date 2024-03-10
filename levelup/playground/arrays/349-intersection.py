class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        i, j = 0, 0
        intersection_set = set()
        while i < len(nums1):

            if (nums1[i] == nums2[j]):
                intersection_set.add(nums1[i])
                i += 1
                j = 0
                continue
            if j == len(nums2)-1:
                i += 1
                j = 0
                continue
            j += 1
        return list(intersection_set)

# print(Solution().intersection([4,9,5], [9,4,9,8,4]))
print(Solution().intersection([1,2,2,1], [2,2]))
