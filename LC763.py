class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # 结果数组
        results = []
        # 每个元素最后的位置
        last = {}

        # 记录每个元素在S中的最后位置
        for i in range(len(S) - 1, -1, -1):
            if S[i] not in last:
                last[S[i]] = i

        i = 0  # 位置指针
        span = 0  # 当前分段的长度
        while i < len(S):
            j = last[S[i]]  # 取出当前i指向元素最后出现位置
            span = 1  # 长度重置为1
            while i != j:
                i += 1
                span += 1
                j = max(j, last[S[i]])  # 对比下一个字母在S中出现的之后位置是否超过位置j
            results.append(span)
            i += 1

        return results