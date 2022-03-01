from linkedList import LinkedList


def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next 
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode


class Solution:
    def reverseLinkedList(self, head):
        prev = None 
        node = head 

        while node is not None:
            nextNode = node.next 
            node.next = prev 
            prev = node 
            node = nextNode 

        return prev


if __name__ == '__main__':
    node0 = LinkedList(0)
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)
    node5 = LinkedList(5)

    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # print(reverseLinkedList(node0)) # 5 -> 4 -> 3 -> 2 -> 1

    s = Solution()
    print(s.reverseLinkedList(node0))