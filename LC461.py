class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xorNumber = x ^ y
        binXorNumber = bin(xorNumber)
        count = binXorNumber.count('1')
        return count