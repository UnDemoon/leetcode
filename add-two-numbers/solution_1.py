# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        next_position = 0
        p1 = l1
        p2 = l2
        p = None
        start = None
        while p1 or p2 or next_position:
            value_1 = p1.val if p1 else 0
            value_2 = p2.val if p2 else 0
            tmp_sum = value_1 + value_2 + next_position
            current_position = tmp_sum % 10
            next_position = int(tmp_sum / 10)
            tmp = ListNode(current_position, None)
            if p:
                p.next = tmp
            if not start:
                start = tmp
            p = tmp
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return start


def nodeInit(node_list: list):
    p = None
    while len(node_list) > 0:
        p = ListNode(node_list.pop(), p)
    return p


if __name__ == '__main__':
    list_1 = [2, 4, 3]
    list_2 = [5, 6, 4]
    n1 = nodeInit(list_1)
    n2 = nodeInit(list_2)
    solu = Solution()
    res = solu.addTwoNumbers(n1, n2)
    temp = res
    while temp:
        print(temp.val)
        temp = temp.next
