"""
设计函数 func_sun(a, b), 求和？

a = 3, b = 4
5

a = 2, b = -4
-2


class Solution:
    def func_sum(self, a: int, b: int) -> int:

"""


class Solution:
    def func_sum(self, a: int, b: int) -> int:
        return a + b

    @staticmethod
    def check_class(solution=None):
        if solution is None:
            solution = Solution
        assert solution().func_sum(a=3, b=4) == 7
        assert solution().func_sum(a=2, b=-4) == -2

    def check_func(self, func=None):
        """

        :param func:
        :return:
        """
        if func is None:
            func = self.func_sum
        assert func(a=3, b=4) == 7
        assert func(a=2, b=-4) == -2


if __name__ == '__main__':
    c = Solution()
    c.check_func(func=c.func_sum)

    # or
    Solution.check_class(solution=Solution)
