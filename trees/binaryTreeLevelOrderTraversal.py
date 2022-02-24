from typing import List, Optional
from nodeDepths import BinaryTreeNode
from collections import defaultdict, deque


class Solution:
    def zigzag(self, root: Optional[BinaryTreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = [[root.value]]
        queue = deque()
        queue.append(root)
        level = 1

        while len(queue) > 0:
            n = len(queue)

            newLevel = []
            for _ in range(n):
                currentNode = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)
                    newLevel.append(currentNode.left.value)
                if currentNode.right:
                    queue.append(currentNode.right)
                    newLevel.append(currentNode.right.value)

            if newLevel:
                level += 1

            if newLevel and level % 2 != 0:
                result.append(newLevel)
            elif newLevel and level  % 2 == 0:
                newLevel.reverse()
                result.append(newLevel)

        return result


    def solution2(self, root):
        if root is None:
            return []

        level = 0
        dict_level = defaultdict(deque)
        queue = deque([root])

        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if level % 2 != 0:
                    dict_level[level].appendleft(node.value)
                else:
                    dict_level[level].append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return dict_level.values()



if __name__ == '__main__':

    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)

    node1.left = node2 
    node1.right = node3 
    node2.left = node4 
    node2.right = node5 

    s = Solution()
    # print(s.zigzag(node1))
    print(s.solution2(node1))