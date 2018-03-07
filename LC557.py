class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for eachWord in s.split():
            reverseWord = eachWord[::-1]
            result.append(reverseWord)

        return ' '.join(result)
