class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res_list = []
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            n1 = nums1[i] if i < len(nums1) else None
            n2 = nums2[j] if j < len(nums2) else None
            if n1 is None and n2 is None:
                raise Exception('运行异常')
            elif n1 is not None and n2 is None:
                res_list.append(n1)
                i += 1
            elif n2 is not None and n1 is None:
                res_list.append(n2)
                j += 1
            else:
                if n1 == n2:
                    res_list.append(n1)
                    res_list.append(n2)
                    i += 1
                    j += 1
                elif n1 < n2:
                    res_list.append(n1)
                    i += 1
                else:
                    res_list.append(n2)
                    j += 1
        if len(res_list) % 2 == 0:
            m_index = int(len(res_list) / 2)
            return float((res_list[m_index - 1] + res_list[m_index]) / 2)
        else:
            return float(res_list[int(len(res_list) / 2)])


if __name__ == '__main__':
    #   测试用例
    l1 = []
    l2 = [0]
    #   运行
    sulution = Solution()
    res = sulution.findMedianSortedArrays(l1, l2)
    print(res)
