class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        elementCount = 0
        for row in range(len(nums)):
            elementCount += len(nums[row])

        if r * c == elementCount:
            tmp = []
            for row in range(len(nums)):
                tmp += nums[row]

            result = []
            for i in range(r):
                thisRow = []
                for j in range(c):
                    thisRow.append(tmp[i * c + j])
                result.append(thisRow)

            return result
        else:
            return nums
