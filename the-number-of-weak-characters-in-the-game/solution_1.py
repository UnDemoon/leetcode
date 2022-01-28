import json
import time
import utils as tool

import numpy as np

'''
第一类递减排序，第二列递增排序
循环时后一个第一列一定小于等于前一个
第一列相等的情况下，第二列后一个一定大于前一个（不重复）
这样判断防御力如果小于max 就是弱角色，因为同一列情况，防御肯定是大于max的,只有跨了列才会小于
'''


class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_def = 0
        for _, def_ in properties:
            if max_def > def_:
                print([_, def_], max_def)
                ans += 1
            else:
                print('-', [_, def_], max_def)
                max_def = max(max_def, def_)
        return ans


if __name__ == '__main__':
    #   测试用例
    test = [[10, 4], [10, 7], [7, 5], [7, 9], [7, 10], [6, 9]]
    time_test = json.loads(tool.loadFile('long_test.txt'))  # 运行
    start = time.time()
    sulution = Solution()
    res = sulution.numberOfWeakCharacters(time_test)
    end = time.time()
    print('\n')
    print('|res|', res)
    print('|time|', end - start)
