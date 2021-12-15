from linkedList import LinkedList


# O(n) TC | O(1) SC where n is the number of nodes in the linked list.
def removeDuplicates(linkedList):
    """
    Returns a modified version of LL that doesn't contain any nodes with
    duplicate values.
    """
    if linkedList  is None:
        return linkedList

    seenNumbersDict = {}
    currNode = linkedList
    prevNode = currNode

    while currNode is not None:
        # If we've seen this node value before...
        if currNode.value in seenNumbersDict:
            prevNode.next = currNode.next
        else:
            seenNumbersDict[currNode.value] = True

        prevNode = currNode
        # Move to next node
        currNode = currNode.next

    return linkedList

def removeDuplicatesCorrect(linkedList):
    """
    The provided solution on AE.

    The inner while loop is looking for the next distinct node,
    instead of just moving next pointers one by one.
    """
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next 
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next 

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode

    return linkedList


if __name__ == '__main__':
    node1 = LinkedList(1)
    node2 = LinkedList(1)
    node1.next = node2

    node3 = LinkedList(3)
    node2.next = node3
    node4 = LinkedList(4)
    node3.next = node4

    node5 = LinkedList(4)
    node4.next = node5
    node6 = LinkedList(4)
    node5.next = node6

    node7 = LinkedList(5)
    node6.next = node7
    node8 = LinkedList(6)
    node7.next = node8

    node9 = LinkedList(6)
    node8.next = node9


    print(f'Before remove: {node1}')
    print(removeDuplicatesCorrect(node1))
    print(f'After remove: {node1}')