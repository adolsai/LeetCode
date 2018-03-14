class Solution:

    result = 0

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def slices(a, i):
            """
            :param a:
            :param i:
            :return:
            """
            if i < 2:
                return 0;

            ap = 0
            if a[i] - a[i - 1] == a[i - 1] - a[i - 2]:
                ap = 1 + slices(a, i - 1)
                self.result += ap
            else:
                slices(a, i - 1)

            return ap

        slices(A, len(A) - 1)

        return self.result