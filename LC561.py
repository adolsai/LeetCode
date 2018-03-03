class Solution(object):

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #排序
        sortedNums = sorted(nums)

        result = 0

        #拿单数需要的值相加
        for index in range(len(sortedNums)):
            if index % 2 == 0:
                result += sortedNums[index]

        return result
