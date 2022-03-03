from linkedList import LinkedList


def removeKthNodeFromEnd(head, k):
    counter = 1
    firstNode = head 
    secondNode = head 

    while counter <= k:
        secondNode = secondNode.next
        counter += 1
    if secondNode is None:
        # Remove head
        head.value = head.next.value
        head.next = head.next.next 
        return 
    while secondNode.next is not None:
        secondNode = secondNode.next 
        firstNode = firstNode.next 

    firstNode.next = firstNode.next.next
    print('hello')


class Solution:
    def removeNthNodeFromEnd(self, head, n):
        dummy = LinkedList(-1)
        dummy.next = head 
        left = dummy
        right = head 

        while right and n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next 
            right = right.next

        left.next = left.next.next
        return dummy.next

        
if __name__ == '__main__':
    node1 = LinkedList(1)
    # node2 = LinkedList(2)
    # node3 = LinkedList(3)
    # node4 = LinkedList(4)
    # node5 = LinkedList(5)

    # node1.next = node2
    # node2.next = node3
    # node3.next = node4 
    # node4.next = node5
    # print(removeKthNodeFromEnd(node1, 2))

    s = Solution()
    print(s.removeNthNodeFromEnd(node1, 1))