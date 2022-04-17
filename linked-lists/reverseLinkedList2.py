from typing import Optional
from linkedList import LinkedList


class Solution:
    def reverseLL(self, head: Optional[LinkedList]) -> Optional[LinkedList]:
        prev = None 
        curr = head 
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        return prev

    def reverseRecursive(self, head):
        if not head:
            return None 

        newHead = head 
        if head.next:
            newHead = self.reverseRecursive(head.next)
            head.next.next = head 
        head.next = None 
        return newHead


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)


    s = Solution()
    print(s.reverseRecursive(head))
    # print(s.reverseLL(head))