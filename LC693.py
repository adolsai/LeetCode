class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        num = n ^ (n >> 1)
        return not (num & (num + 1))

