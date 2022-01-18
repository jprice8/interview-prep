def permutations(array):
    permuations = []
    result = permuationHelper(array, [], permuations)

def permuationHelper(array, currentPermuation, permuations):
    if not len(array) and len(currentPermuation):
        permuations.append(currentPermuation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1 :]
            newPermutation = currentPermuation + [array[i]]
            permuationHelper(newArray, newPermutation, permuations)


if __name__ == '__main__':
    array = [1, 2, 3]
    print(permutations(array))