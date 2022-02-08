class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        conf = [
            [a, 'a'],
            [b, 'b'],
            [c, 'c'],
        ]
        res_str = ""
        while True:
            conf.sort(key=lambda x: x[0], reverse=True)
            if not self.sameChar(res_str, conf[0][1]) and conf[0][0] > 0:
                res_str += conf[0][1]
                conf[0][0] -= 1
            elif not self.sameChar(res_str, conf[1][1]) and conf[1][0] > 0:
                res_str += conf[1][1]
                conf[1][0] -= 1
            elif not self.sameChar(res_str, conf[2][1]) and conf[2][0] > 0:
                res_str += conf[2][1]
                conf[2][0] -= 1
            else:
                break
        return res_str

    def sameChar(self, t_str: str, char: str) -> bool:
        is_same = False
        if len(t_str) >= 2:
            char_1 = t_str[-1]
            char_2 = t_str[-2]
            if char_1 == char_2 == char:
                is_same = True
        return is_same


if __name__ == '__main__':
    #   测试用例
    a = 5
    b = 4
    c = 3
    #   运行
    sulution = Solution()
    res = sulution.longestDiverseString(a, b, c)
    print(res)
