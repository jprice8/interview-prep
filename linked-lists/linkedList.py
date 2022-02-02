

class LinkedList:
    """
    LinkedList is our node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        result = []
        curr = self
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        return repr(result)

    def printNodes(self):
        node = self 
        while node is not None:
            print(node.value)
            node = node.next


