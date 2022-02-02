class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None 
        self.next = None 

    def __repr__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __repr__(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next 
        
        return repr(result)

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node 
            self.tail = node
            return 
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return 
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        # If node to insert is head and tail
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return 

        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev 
        nodeToInsert.next = node 
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)
        nodeToInsert.prev = node 
        nodeToInsert.next = node.next 
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return 
        node = self.head 
        currentPosition = 1
        while currentPosition != position:
            node = node.next 
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head 
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        """
        If node to remove is head, set next.
        If node to remove is tail, set prev.
        Else, call helper function.
        """
        if node == self.head:
            self.head = self.head.next 
        if node == self.tail:
            self.tail = self.tail.prev 
        self.removeNodeBindings(node)

    def removeNodeBindings(self, node):
        """
        Helper function:
            If there's a previous node, set it's next to current next.
            If there's a next node, set it's prev to current prev.
            Clear the links from current node to prev and next.
        """
        if node.prev is not None:
            node.prev.next = node.next 
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None 
        node.next = None

    def containsNodeWithValue(self, value):
        node = self.head 
        while node is not None and node.value != value:
            node = node.next 
        return node is not None


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # Stand alone nodes
    node3a = Node(3)
    node3b = Node(3)
    node6 = Node(6)

    linkedList = DoublyLinkedList()

    # Construct doubly linked list
    print(linkedList.setTail(node1))
    print(linkedList.setTail(node2))
    print(linkedList.setTail(node3))
    print(linkedList.setTail(node4))
    print(linkedList.setTail(node5))

    linkedList.insertAtPosition(2, node6)


