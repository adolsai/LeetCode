class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 第一行字母集合
        a = set('qwertyuiop')
        # 第二行字母集合
        b = set('asdfghjkl')
        # 第三行字母集合
        c = set('zxcvbnm')

        ans = []

        for word in words:
            # 当前单词的字母集合, 因为是集合所以会去重
            t = set(word.lower())
            if a & t == t:  # 第一行检查
                ans.append(word)
            if b & t == t:  # 第二行检查
                ans.append(word)
            if c & t == t:  # 第三行检查
                ans.append(word)
        return ans