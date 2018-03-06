class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 仅统计每一个战舰左上角的X
                if board[i][j] == 'X':
                    flag = 1
                    # 检测上方位置是否为X
                    if j > 0 and board[i][j - 1] == 'X':
                        flag = 0
                    # 检测左方位置是否为X
                    if i > 0 and board[i - 1][j] == 'X':
                        flag = 0

                    result += flag
        return result
