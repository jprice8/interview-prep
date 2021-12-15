# Binary Tree problem 1 on algoexpert

class BinaryTree:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

    def insert(self, values, i=0):
        if i >= len(values):
            return 
        queue = [self]

        while len(queue) > 0:
            current = queue.pop()
            if current.left is None:
                current.left = BinaryTree(values[i])
                break 
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break 
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def branchSums(root):
        sums = []
        calculateBranchSums(root, 0, sums)
        return sums 

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return 

    newRunningSum = runningSum + node.value 
    if node.left is None and node.right is None:
        # We've hit a leaf node, time to sum
        sums.append(newRunningSum)
        return 

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)


tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
print(branchSums(tree))