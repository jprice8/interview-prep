from linkedList import LinkedList


def findLoop(head):
    first = head.next 
    second = head.next.next 
    while first != second:
        first = first.next 
        second = second.next.next
    first = head 
    while first != second:
        first = first.next 
        second = second.next 
    return first


if __name__ == '__main__':
    node0 = LinkedList(0)
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)
    node5 = LinkedList(5)
    node6 = LinkedList(6)
    node7 = LinkedList(7)
    node8 = LinkedList(8)
    node9 = LinkedList(9)

    node0.next = node1 
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node4

    print(findLoop(node1))