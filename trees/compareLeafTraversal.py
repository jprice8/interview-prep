from nodeDepths import BinaryTreeNode


def compareLeafTraversal(tree1, tree2):
     treeOneLeafs = traverseLeafs(tree1, [])
     print(treeOneLeafs)
     treeTwoLeafs = traverseLeafs(tree2, [])
     print(treeTwoLeafs)

     return treeOneLeafs == treeTwoLeafs


def traverseLeafs(node, nodeList):
    if node is None:
        return

    traverseLeafs(node.left, nodeList)
    traverseLeafs(node.right, nodeList)

    isLeaf = node.left == None and node.right == None 

    if isLeaf:
        nodeList.append(node.value)

    return nodeList


if __name__ == '__main__':
    nodeA1 = BinaryTreeNode(1)
    nodeA2 = BinaryTreeNode(2)
    nodeA3 = BinaryTreeNode(3)
    nodeA4 = BinaryTreeNode(4)
    nodeA5 = BinaryTreeNode(5)
    nodeA6 = BinaryTreeNode(6)
    nodeA7 = BinaryTreeNode(7)
    nodeA8 = BinaryTreeNode(8)

    nodeA1.left = nodeA2 
    nodeA1.right = nodeA3 

    nodeA2.left = nodeA4 
    nodeA2.right = nodeA5 

    nodeA3.right = nodeA6 

    nodeA5.left = nodeA7 
    nodeA5.right = nodeA8 

    nodeB1 = BinaryTreeNode(1)
    nodeB2 = BinaryTreeNode(2)
    nodeB3 = BinaryTreeNode(3)
    nodeB4 = BinaryTreeNode(4)
    nodeB5 = BinaryTreeNode(5)
    nodeB6 = BinaryTreeNode(6)
    nodeB7 = BinaryTreeNode(7)
    nodeB8 = BinaryTreeNode(8)
    nodeB9 = BinaryTreeNode(9)

    nodeB1.left = nodeB2 
    nodeB1.right = nodeB3 

    nodeB2.left = nodeB4 
    nodeB2.right = nodeB7 

    nodeB3.right = nodeB5 

    nodeB5.left = nodeB8 
    nodeB5.right = nodeB6

    # nodeB8.left = nodeB9

    print(compareLeafTraversal(nodeA1, nodeB1))