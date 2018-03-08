class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for num in range(1, n + 1):
            if num % 3 == 0:
                if num % 5 == 0:
                    result.append('FizzBuzz')
                else:
                    result.append('Fizz')
            elif num % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(num))

        return result
