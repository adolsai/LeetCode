class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        candiesSet = set(candies)

        if len(candiesSet) > len(candies) / 2:
            return int(len(candies) / 2)
        else:
            return len(candiesSet)
