def numberWaysTraverseGraph(width, height):
    if width == 1 or height == 1:
        return 1

    return numberWaysTraverseGraph(width - 1, height) + numberWaysTraverseGraph(width, height - 1)

width = 2
height = 3
print(numberWaysTraverseGraph(width, height))