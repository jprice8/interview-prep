# Worst case: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def permutations(array):
    permutations = []
    permuationHelper(array, [], permutations)
    return permutations

def permuationHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1 :]
            newPermutation = currentPermutation + [array[i]]
            permuationHelper(newArray, newPermutation, permutations)


if __name__ == '__main__':
    array = [1, 2, 3]
    print(permutations(array))