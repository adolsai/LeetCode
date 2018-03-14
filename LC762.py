class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        def checkIfPrime(num):
            """
            :type num: int
            :rtype: bool
            """

            if (num <= 1):
                return False

            square_num = math.floor(num ** 0.5)
            for i in range(2, (square_num + 1)):
                if (num % i) == 0:
                    return False

            return True

        result = 0
        for num in range(L, R + 1):
            if checkIfPrime(str(bin(num)).count('1')):
                result += 1

        return result