from glossary import AncestralTree


def new_trees():
    ancestralTrees = {}
    for letter in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        ancestralTrees[letter] = AncestralTree
    return ancestralTrees


def youngestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor) 
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant


if __name__ == '__main__':
    # trees = new_trees()
    # trees['A'].addDescendants(trees['B'], trees['C'])

    treeA = AncestralTree('A')
    treeB= AncestralTree('B')
    treeC = AncestralTree('C')
    treeD = AncestralTree('D')
    treeE = AncestralTree('E')
    treeF = AncestralTree('F')
    treeG = AncestralTree('G')
    treeH = AncestralTree('H')
    treeI = AncestralTree('I')

    treeB.ancestor = treeA
    treeC.ancestor = treeA 

    treeD.ancestor = treeB 
    treeE.ancestor = treeB 

    treeF.ancestor = treeC 
    treeG.ancestor = treeC 

    treeH.ancestor = treeD 
    treeI.ancestor = treeD

    print(youngestCommonAncestor(treeA, treeE, treeI))