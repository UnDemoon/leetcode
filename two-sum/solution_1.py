class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = len(nums) - 1
        while i > 0:
            temp = target - nums.pop()
            if temp in nums:
                return [nums.index(temp), i]
            i -= 1


if __name__ == '__main__':
    sulution = Solution()
    num_list = [3, 2, 4]
    target = 6
    res = sulution.twoSum(num_list, target)
    print(res)
