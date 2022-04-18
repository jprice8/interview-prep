from typing import Optional
from linkedList import LinkedList


class Solution:
    def reorder(self, head: Optional[LinkedList]) -> None:
        # find middle node
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # reverse remaining list from slow node
        prev = None
        while slow:
            nxt = slow.next 
            slow.next = prev 
            prev = slow 
            slow = nxt 

        # merge sorted lists
        first, second = head, prev
        while second.next:
            nxt = first.next 
            first.next = second 
            first = nxt 

            nxt = second.next 
            second.next = first 
            second = nxt


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    s = Solution()
    print(s.reorder(head))