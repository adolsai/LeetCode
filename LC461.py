class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #先异或
        xorNumber = x ^ y
        #转二进制
        binXorNumber = bin(xorNumber)
        #计算1的个数
        count = binXorNumber.count('1')
        return count