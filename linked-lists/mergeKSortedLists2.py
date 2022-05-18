from ListNode import ListNode
from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None 

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None 
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy 

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 
                l1 = l1.next 
            else:
                tail.next = l2
                l2 = l2.next 
            tail = tail.next 

        if l1:
            tail.next = l1 
        elif l2:
            tail.next = l2 
        
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(7)

    l2 = ListNode(2)
    l2.next = ListNode(5)
    l2.next.next = ListNode(8)

    l3 = ListNode(3)
    l3.next = ListNode(6)
    l3.next.next = ListNode(9)

    s = Solution()
    print(s.mergeKLists([l1, l2, l3]))