from linkedList import LinkedList


class Solution:
    def linkedListCycle(self, head):
        fastPtr = head 
        slowPtr = head 
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

            if fastPtr == slowPtr:
                return True 

        return False


if __name__ == '__main__':
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)
    node5 = LinkedList(5)

    node1.next = node2 
    node2.next = node3 
    node3.next = node4
    node4.next = node5 
    node5.next = node2

    s = Solution()
    print(s.linkedListCycle(node1))