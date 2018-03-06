class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for eachNumber in range(num + 1):
            binNumber = bin(eachNumber)
            count = binNumber.count('1')
            result.append(count)

        return result