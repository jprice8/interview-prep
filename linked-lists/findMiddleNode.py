from linkedList import LinkedList


def findMiddleNode(head):
    fastNode = head
    slowNode = head
    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode.value


if __name__ == '__main__':
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(findMiddleNode(node1))