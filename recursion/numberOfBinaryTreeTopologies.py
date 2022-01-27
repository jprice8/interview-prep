#### Brute force
def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1 

    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    return numberOfTrees


#### Top down recursion ####
# O(n^2) time | O(n) space
def aeSolutionRecursion(n, cache={0: 1}):
    if n in cache:
        return cache[n]
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTrees = aeSolutionRecursion(leftTreeSize, cache)
        numberOfRightTrees = aeSolutionRecursion(rightTreeSize, cache)
        numberOfTrees = numberOfLeftTrees * numberOfRightTrees
    cache[n] = numberOfTrees
    return numberOfTrees


#### Bottom up iteration (tabulation) ####
# O(n^2) time | O(n) space
def aeSolutionIterative(n):
    cache = [1]
    for m in range(1, n + 1):
        numberOfTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = m - 1 - leftTreeSize
            numberOfLeftTrees = cache[leftTreeSize]
            numberOfRightTrees = cache[rightTreeSize]
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(numberOfTrees)
    return cache[n]


if __name__ == '__main__':
    print(aeSolutionIterative(2))