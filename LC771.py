class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for idx, item in enumerate(S):
            if item in J:
                result += 1

        return result
