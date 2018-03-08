class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        #行
        for i in range(len(matrix) - 1):
            #列
            for j in range(len(matrix[0]) - 1):
                #检查当前元素值是否等于右下角元素值
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
