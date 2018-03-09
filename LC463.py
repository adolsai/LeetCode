class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0

        r = len(grid)
        c = 0

        if (r > 0):
            c = len(grid[0])

        # 遍历每一个点
        for i in range(r):
            for j in range(c):
                # 值为1, 判断周围的数值
                if grid[i][j] == 1:
                    # 上
                    if i - 1 < 0:  # 上面没有格子了, 即边界
                        result += 1
                    elif grid[i - 1][j] == 0:  # 上面是0, 即边界
                        result += 1

                    # 下
                    if i + 1 >= r:  # 下面没有格子了, 即边界
                        result += 1
                    elif grid[i + 1][j] == 0:  # 下面是0, 即边界
                        result += 1

                    # 左
                    if j - 1 < 0:  # 左边没有格子了, 即边界
                        result += 1
                    elif grid[i][j - 1] == 0:  # 左边是0, 即边界
                        result += 1

                    # 右
                    if j + 1 >= c:  # 右边没有格子了, 即边界
                        result += 1
                    elif grid[i][j + 1] == 0:  # 右边是0, 即边界
                        result += 1

        return result


