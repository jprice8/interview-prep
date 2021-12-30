from nodeDepths import BinaryTreeNode

# Using BFS here
def findNodesDistanceKbfs(tree, target, k):
    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)

    return breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)


def breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
    # Mention to interviewer that you would normally use a deque for optimal pop.
    # Popping from front of list is O(n). Normally a queue would give us O(1).
    queue = [(targetNode, 0)]
    seen = {targetNode.value}
    while len(queue) > 0:
        currentNode, distanceFromTarget = queue.pop(0)
        # If we find distance to K, we know all other nodes in queue must be same distance.
        # This is due to BFS.
        if distanceFromTarget == k:
            nodesDistanceK = [node.value for node, _ in queue]
            nodesDistanceK.append(currentNode.value)
            return nodesDistanceK

        connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
        for node in connectedNodes:
            if node is None:
                continue 

            if node.value in seen:
                continue 

            seen.add(node.value)
            queue.append((node, distanceFromTarget + 1))

    return []


def getNodeFromValue(value, tree, nodesToParents):
    if tree.value == value:
        return tree 
    
    nodeParent = nodesToParents[value]
    if nodeParent.left is not None and nodeParent.left.value == value:
        return nodeParent.left 

    return nodeParent.right


# O(n) time | O(n) space - where n is the number of nodes in the tree
def populateNodesToParents(node, nodesToParents, parent=None):
    if node is not None:
        nodesToParents[node.value] = parent
        populateNodesToParents(node.left, nodesToParents, node)
        populateNodesToParents(node.right, nodesToParents, node)


#### Recursive DFS solution ####
def findNodesDistanceKdfs(tree, target, k):
    nodesDistanceK = []
    findDistanceFromNodeToTarget(tree, target, k, nodesDistanceK)
    return nodesDistanceK


def findDistanceFromNodeToTarget(node, target, k, nodesDistanceK):
    if node is None:
        return -1 
    
    if node.value == target:
        addSubtreeNodesAtDistanceK(node, 0, k, nodesDistanceK)
        return 1

    leftDistance = findDistanceFromNodeToTarget(node.left, target, k, nodesDistanceK)
    rightDistance = findDistanceFromNodeToTarget(node.right, target, k, nodesDistanceK)

    if leftDistance == k or rightDistance == k:
        nodesDistanceK.append(node.value)

    if leftDistance != -1:
        addSubtreeNodesAtDistanceK(node.right, leftDistance + 1, k, nodesDistanceK)
        return leftDistance + 1

    if rightDistance != -1:
        addSubtreeNodesAtDistanceK(node.left, rightDistance + 1, k, nodesDistanceK)
        return rightDistance + 1

    return -1


def addSubtreeNodesAtDistanceK(node, distance, k, nodesDistanceK):
    if node is None:
        return 

    if distance == k:
        nodesDistanceK.append(node.value)
    else:
        addSubtreeNodesAtDistanceK(node.left, distance + 1, k, nodesDistanceK)
        addSubtreeNodesAtDistanceK(node.right, distance + 1, k, nodesDistanceK)


if __name__ == '__main__':
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node1.left = node2
    node1.right = node3

    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node2.left = node4 
    node2.right = node5

    node6 = BinaryTreeNode(6)
    node3.right = node6

    node7 = BinaryTreeNode(7)
    node8 = BinaryTreeNode(8)
    node6.left = node7 
    node6.right = node8

    target = 3
    k = 2
    expected = [2, 7, 8]
    print(findNodesDistanceKdfs(node1, target, k))