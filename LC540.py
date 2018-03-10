class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
