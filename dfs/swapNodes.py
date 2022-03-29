from collections import deque
import os


# Hackerrank question Swap Nodes
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None

def buildTree(indexes):
    f = lambda x: None if x == -1 else Node(x)
    children = [list(map(f, x)) for x in indexes]
    nodes = {n.data: n for n in filter(None, sum(children, []))}
    nodes[1] = Node(1)
    for idx, child_pair in enumerate(children):
        nodes[idx + 1].left = child_pair[0]
        nodes[idx + 1].right = child_pair[1]
    return nodes[1]

def inorder(root):
    stack = []
    curr = root 
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left 
        elif stack:
            curr = stack.pop()
            yield curr.data 
            curr = curr.right

def swap_nodes(indexes, queries):
    root = buildTree(indexes)
    for k in queries:
        h = 1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if h % k == 0:
                    node.left, node.right = node.right, node.left 
                q += filter(None, (node.left, node.right))
            h += 1
        yield inorder(root)


if __name__ == '__main__':
    # print('hello world')
    # n = int(input('please enter n').strip())

    # indexes = []

    # for _ in range(n):
    #     indexes.append(list(map(int, input('Please enter index map').rstrip().split())))

    # queries_count = int(input('please enter query count').strip())

    # queries = []

    # for _ in range(queries_count):
    #     queries_item = int(input('please enter queries item').strip())
    #     queries.append(queries_item)
    indexes = [[2, 3], [-1, -1], [-1, -1]]
    queries = [1, 1]

    print(swapNodes(indexes, queries))

