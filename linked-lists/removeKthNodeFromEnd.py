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
    while secondNode is not None:
        secondNode = secondNode.next 
        firstNode = firstNode.next 

    firstNode.next = firstNode.next.next



        
if __name__ == '__main__':
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)

    node1.next = node2 
    node2.next = node3 
    node3.next = node4
    print(removeKthNodeFromEnd(node1, 2))