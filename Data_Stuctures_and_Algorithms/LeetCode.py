# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        result = root
        excess = 0
        while l1 or l2 or excess:
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next

            result.next = ListNode(excess % 10)
            result = result.next
            excess = excess // 10

        return root.next


# l1 = [2,4,3]
# l2 = [5,6,4]

val = Solution()
result = val.addTwoNumbers(l1, l2)

print(result)
