import math


class Solution:
    def myAtoi(self, s: str) -> int:
        num_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        char_list = []
        char_mark = ''
        i = 0
        while i < len(s):
            t_char = s[i]
            if t_char == ' ':
                i += 1
                continue
            elif t_char in num_char:
                if t_char != '0':
                    char_list.append(t_char)
                elif len(char_list) > 0:
                    char_list.append(t_char)
            elif t_char in ['-', '+']:
                if len(char_list) == 0 and not char_mark:
                    char_mark = t_char
                else:
                    break
            else:
                break
            i += 1
        num_str = char_mark + ''.join(char_list) if len(char_list) > 0 else 0
        num = int(num_str)
        if num < math.pow(-2, 31):
            num = math.pow(-2, 31)
        if num > (math.pow(2, 31) - 1):
            num = (math.pow(2, 31) - 1)
        return int(num)


if __name__ == '__main__':
    #   测试用例
    test_str = "00000-42a1234"
    #   运行
    sulution = Solution()
    res = sulution.myAtoi(test_str)
    print(res)
