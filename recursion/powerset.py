# O() time | O() space
def powersetIterative(array):
    subsets = [[]] 
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets


# O(n*2^n) time | O(n*2^n) space
def powersetRecursive(array, idx=None):
    if idx is None:
        idx = len(array) - 1

    if idx < 0:
        return [[]]

    ele = array[idx]
    subsets = powersetRecursive(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets
    


if __name__ == '__main__':
    array = [1, 2, 3]
    print(powersetIterative(array))