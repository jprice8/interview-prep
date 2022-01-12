class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right

# O(n^2) time | O(n) space - where n is the length of input array.
# def reconstructBst(preOrderTraversalValues):
#     if len(preOrderTraversalValues) == 0:
#         return None 

#     currentValue = preOrderTraversalValues[0] 
#     rightSubtreeRootIdx =  len(preOrderTraversalValues)

#     for idx in range(1, len(preOrderTraversalValues)):
#         value = preOrderTraversalValues[idx]
#         if value >= currentValue:
#             rightSubtreeRootIdx = idx 
#             break 

#     leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
#     rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])
#     return BST(currentValue, leftSubtree, rightSubtree)


class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx


# O(n) time | O(n) space - where n is the length of potv array.
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)


def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None 
    
    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None 

    currentSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree)


if __name__ == '__main__':
    root = reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])
    print(root.value)