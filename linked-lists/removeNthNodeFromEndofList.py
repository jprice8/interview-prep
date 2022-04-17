from typing import Optional
from linkedList import LinkedList


class Solution:
    def removeNth(self, head: Optional[LinkedList], n: int) -> Optional[LinkedList]:
        dummy = LinkedList(-1)
        dummy.next = head

        left, right = dummy, head
        traverse_count = 0
        # move right into position
        while traverse_count < n:
            right = right.next
            traverse_count += 1

        # traverse left and right to end of list
        while right:
            right = right.next
            left = left.next

        # adjust pointers
        left.next = left.next.next
        return dummy.next


if __name__ == '__main__':
    # head = LinkedList(1)
    # head.next = LinkedList(2)
    # head.next.next = LinkedList(3)
    # head.next.next.next = LinkedList(4)
    # head.next.next.next.next = LinkedList(5)

    head = LinkedList(1)
    head.next = LinkedList(2)

    s = Solution()
    print(s.removeNth(head, 1)) # 1, 2, 3, 5