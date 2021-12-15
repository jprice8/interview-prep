class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        """
        Insert node into BST.
        """
        currentNode = self
        while True:
            if value < currentNode.value:
                # Traverse left branch
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

            else:
                # Traverse right branch
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value: int):
        """
        Search the BST for a given value.
        """
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                # Traverse left branch
                currentNode = currentNode.left
            elif value > currentNode.value:
                # Traverse right branch
                currentNode = currentNode.right
            else:
                # We found the value
                return True

        return False

    def remove(self, value: int, parentNode=None):
        """
        Remove a given value from the BST.
        Two step process:
        1. Find target node.
        2. Delete and reassign.
        """
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                # Traverse left branch
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                # Traverse right branch
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # We found the node
                if self.left is not None and self.right is not None:
                    self.value = self.right.getMinValue()
                    self.right.remove(self.value, self)
                elif parentNode is None:
                    # If root node
                    if self.left is not None:
                        # If left subtree
                        self.value = self.left.value
                        self.right = self.left.right
                        self.left = self.right.right

                    elif self.right is not None:
                        # If right subtree
                        self.value = self.right.value
                        self.left = self.right.left
                        self.right = self.right.right

                    else:
                        # This is a single node tree; do nothing.
                        pass

                elif parentNode.left == self:
                    parentNode.left = self.left if self.left is not None else self.right
                elif parentNode.right == self:
                    parentNode.right = self.left if self.left is not None else self.right

            return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
