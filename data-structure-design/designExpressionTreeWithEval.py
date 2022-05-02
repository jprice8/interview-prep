from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        if self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '/':
            return self.left.evaluate() // self.right.evaluate()


class TreeBuilder:
    def buildTree(self, postfix: List[str]) -> Node:
        # 1) Loop through postfix, keep num stack
        # 2) When see operator, call evaluate
        node, stack = None, []
        for item in postfix:
            node = TreeNode(item)
            if not item.isdigit():
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        return node


if __name__ == '__main__':
    postfix = ['4', '5', '2', '7', '+', '-', '*']
    tb = TreeBuilder()
    exp_tree = tb.buildTree(postfix)
    print(exp_tree.evaluate())