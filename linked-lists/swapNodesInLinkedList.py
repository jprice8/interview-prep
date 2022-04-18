from linkedList import LinkedList


class Solution:
    def swapNodes(self, head, k):
        left = LinkedList(-1)
        left.next = head 
        right = head 
        while k > 1:
            right = right.next
            k -= 1
        first = right 
        firstVal = first.value

        # second pass
        while right:
            left = left.next
            right = right.next

        # swap nodes
        second = left 
        secondVal = second.value

        first.value = secondVal
        second.value = firstVal

        return head




if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
    s = Solution()
    print(s.swapNodes(head, 2))