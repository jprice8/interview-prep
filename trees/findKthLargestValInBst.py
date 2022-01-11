from nodeDepths import BinaryTreeNode


# O(n) time | O(n) space - where n is the number of nodes in the tree.
# def findKthLargestValue(tree, k):
#     nodeList = []
#     traverseTree(tree, nodeList)
#     # Index with k from end
#     return nodeList[-k]


# def traverseTree(tree, nodeList):
#     if tree is None:
#         return 

#     traverseTree(tree.left, nodeList)
#     nodeList.append(tree.value)
#     traverseTree(tree.right, nodeList)


class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue


def findKthLargestValue(tree, k):
    treeInfo = TreeInfo(0, -1)
    traverseTreeOptimal(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue

def traverseTreeOptimal(tree, k, treeInfo):
    if tree is None or treeInfo.numberOfNodesVisited >= k:
        return

    traverseTreeOptimal(tree.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = tree.value
        traverseTreeOptimal(tree.left, k, treeInfo)


if __name__ == '__main__':
    node15 = BinaryTreeNode(15)
    nodeA5 = BinaryTreeNode(5)
    node20 = BinaryTreeNode(20)
    node2 = BinaryTreeNode(2)
    nodeB5 = BinaryTreeNode(5)
    node17 = BinaryTreeNode(17)
    node22 = BinaryTreeNode(22)
    node1 = BinaryTreeNode(1)
    node3 = BinaryTreeNode(3)

    node15.left = nodeA5 
    node15.right = node20
    
    nodeA5.left = node2 
    nodeA5.right = nodeB5

    node20.left = node17
    node20.right = node22

    node2.left = node1 
    node2.right = node3

    print(findKthLargestValue(node15, 3))