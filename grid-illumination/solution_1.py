class Bulb:
    def __init__(self, row: int, col: int, light: int, open: int):
        self.row = row
        self.col = col
        self.light = light  # 0没有亮 1亮光
        self.open = open  # 0关闭 1打开


class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        grid = []
        for i in range(n):
            temp = []
            for j in range(n):
                bulb = Bulb(i, j, 0, 0)
                temp.append(bulb)
            grid.append(temp)
        #   打印二维数组
        # for i  in range(n):
        #     for j in range(n):
        #         print(i, j, grid[i][j].light)
        for op in lamps:
            row, col = op
            grid[row][col].open = 1
            for i in range(n):
                grid[row][i].light = 1
            for i in range(n):
                grid[i][col].light = 1
            i = row
            j = col
            while True:
                i -= 1
                j += 1
                if i < 0 or j > n:
                    break
                grid[i][j].light = 1
            i = row
            j = col
            while True:
                i += 1
                j -= 1
                if i > n or j < 0:
                    break
                grid[i][j].light = 1
            i = row
            j = col
            while True:
                i += 1
                j += 1
                if i > n or j > n:
                    break
                grid[i][j].light = 1
            i = row
            j = col
            while True:
                i -= 1
                j -= 1
                if i < 0 or j < 0:
                    break
                grid[i][j].light = 1
        res = []
        for item in queries:
            res.append(grid[item[0]][item[1]].light)
        return res


if __name__ == '__main__':
    #   测试用例
    n = 5
    lamps = [[0, 0], [4, 4]]
    queries = [[1, 2], [3, 3]]
    #   运行
    sulution = Solution()
    res = sulution.gridIllumination(n, lamps, queries)
    print(res)
