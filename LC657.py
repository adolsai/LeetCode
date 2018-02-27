class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical = 0
        horizontol = 0

        for letter in moves:
            if letter == 'U':
                vertical += 1
            elif letter == 'D':
                vertical -= 1
            elif letter == 'L':
                horizontol -= 1
            elif letter == 'R':
                horizontol += 1

        if vertical == 0 and horizontol == 0:
            return True
        else:
            return False
