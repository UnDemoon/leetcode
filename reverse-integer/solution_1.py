import math


class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(abs(x))
        i = len(x_str) - 1
        new_str = ""
        while i >= 0:
            new_str += x_str[i]
            i -= 1
        res_num = int(new_str)
        if x < 0:
            res_num = -res_num
        if res_num < math.pow(-2, 31) or res_num > (math.pow(2, 31) - 1):
            res_num = 0
        return res_num


if __name__ == '__main__':
    #   测试用例
    num = 123
    #   运行
    sulution = Solution()
    res = sulution.reverse(num)
    print(res)
