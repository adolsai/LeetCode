class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums1)):
            num = nums1[i]
            thisResult = -1
            indexOfThisNum = nums2.index(num)
            for j in range(indexOfThisNum, len(nums2)):
                compareNum = nums2[j]
                if num < compareNum:
                    thisResult = compareNum
                    break

            result.append(thisResult)

        return result