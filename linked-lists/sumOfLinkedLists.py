from linkedList import LinkedList

# O(n + m) time | O(n + m) space - where sl is the length of the sum list.
def sumOfLinkedLists(linkedListOne, linkedListTwo):

    node = linkedListOne
    num1 = linkedListToInt(node)

    node = linkedListTwo
    num2 = linkedListToInt(node)

    integerSum = num1 + num2 

    nodeList = intToNodeList(integerSum)
    for idx in range(len(nodeList) - 1):
        currentNode = nodeList[idx]
        nextNode = nodeList[idx + 1]
        currentNode.next = nextNode

    return nodeList[0]


def intToNodeList(num): # 2291
    nodeList = []

    while num > 0:
        listValue = num % 10
        node = LinkedList(listValue)
        nodeList.append(node)
        num //= 10

    return nodeList


def linkedListToInt(node):
    multiplier = 1
    num = 0

    while node is not None:
        num += node.value * multiplier

        multiplier *= 10
        node = node.next

    return num


# O(max(m, n)) time | O(max(m, n)) space - where m and n are the lengths of our lists.
def aeSolution(linkedListOne, linkedListTwo):
    newLinkedListHeadPointer = LinkedList(0) # dummy node, use next pointer to reference new list.
    currentNode = newLinkedListHeadPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode 

        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne is not None else None 
        nodeTwo = nodeTwo.next if nodeTwo is not None else None 

    return newLinkedListHeadPointer.next


if __name__ == '__main__':
    node2a = LinkedList(2)
    node4a = LinkedList(4)
    node7a = LinkedList(7)
    node1a = LinkedList(1)

    node2a.next = node4a
    node4a.next = node7a
    node7a.next = node1a

    node9b = LinkedList(9)
    node4b = LinkedList(4)
    node5b = LinkedList(5)

    node9b.next = node4b
    node4b.next = node5b

    # print(sumOfLinkedLists(node2a, node9b))
    print(aeSolution(node2a, node9b))