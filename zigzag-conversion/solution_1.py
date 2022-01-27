class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        sum_list = []
        for i in range(numRows):
            sum_list.append([])
        sum_index = 0
        setp = 1
        for char in s:
            sum_list[sum_index].append(char)
            if sum_index == 0:
                setp = 1
            if sum_index == len(sum_list) - 1:
                setp = -1
            sum_index += setp
        new_str = ""
        for str_list in sum_list:
            for char in str_list:
                new_str += char
        return new_str


if __name__ == '__main__':
    #   测试用例
    short_s = "ABC"
    rows = 1
    #   运行
    sulution = Solution()
    res = sulution.convert(short_s, rows)
    print(res)
