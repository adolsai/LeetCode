class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #这个想法比我的6多了
        #https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC++Java-Solution
        res = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(p[1],p)
        return res