from linkedList import LinkedList


# O(m + n) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne 
    p1Prev = None 
    p2 = headTwo 

    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            p1Prev = p1 
            p1 = p1.next
        else:
            if p1Prev is not None:
                p1Prev.next = p2
            p1Prev = p2 
            p2 = p2.next
            p1Prev.next = p1 
    if p1 is None:
        p1Prev.next = p2 
    return headOne if headOne.value < headTwo.value else headTwo


if __name__ == '__main__':
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)
    node5 = LinkedList(5)
    node6 = LinkedList(6)
    node7 = LinkedList(7)
    node8 = LinkedList(8)
    node9 = LinkedList(9)
    node10 = LinkedList(10)

    node2.next = node6 
    node6.next = node7 
    node7.next = node8 

    node1.next = node3 
    node3.next = node4 
    node4.next = node5 
    node5.next = node9 
    node9.next = node10 

    print(mergeLinkedLists(node2, node1))