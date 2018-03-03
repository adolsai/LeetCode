class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numList = []
        for num in range(left, right + 1):
            # 逐位检查的临时变量
            numThisTurn = num

            while numThisTurn > 0:
                # 取当前个位值
                elementThisTurn = numThisTurn % 10
                numThisTurn //= 10

                # 整除检查
                if elementThisTurn == 0 or num % elementThisTurn != 0:
                    break

                if numThisTurn == 0:
                    numList.append(num)

        return numList

