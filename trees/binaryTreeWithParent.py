class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left 
        self.right = right 
        self.parent = parent 

    def __repr__(self) -> str:
        return str(self.value)
