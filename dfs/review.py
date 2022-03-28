from TreeNode import TreeNode


def dfs(root, target):
    if root is None:
        return None 
    if root.val == target:
        return root 

    # return non-null return value from the recursive calls
    left = dfs(root.left, target)
    if left is not None:
        return left 

    # at this point, we know left is null and right could be null or non-null
    # We return right recursive call directly because 
    # - if it's non-null we should return it
    # - if it's null, then both left and right are null, we should return null
    return dfs(root.right, target)
    # can be shortened to: return dfs(root.left, target) or dfs(root.right, target)

def dfs1(root, target):
    if root is None:
        return None 
    if root.val == target:
        return root 

    return dfs1(root.left, target) or dfs1(root.right, target)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.left.left.right = TreeNode(5)
    print(dfs1(root, 4))