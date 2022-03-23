from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass 


class TreeNode(Node):
    def evaluate(self) -> int:
        pass 

    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None


class TreeBuilder:
    def buildTree(self, postfix: List[str]) -> Node:
        curr, stack = None, []
        for elem in postfix:
            curr = TreeNode(elem)
            if not elem.isdigit():
                curr.right = stack.pop()
                curr.left = stack.pop()
            stack.append(curr)
        return curr


if __name__ == '__main__':
    postfix = ['3', '4', '+', '2', '*', '7', '/']
    obj = TreeBuilder()
    expTree = obj.buildTree(postfix)
    ans = expTree.evaluate()
    print(ans)