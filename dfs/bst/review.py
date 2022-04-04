from TreeNode import TreeNode


class Solution:
    def find(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return val 

        if val > root.val:
            return self.find(root.right, val)
        else:
            return self.find(root.left, val)

    def insert(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)

    root.right = TreeNode(11)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(13)

    s = Solution()
    print(s.insert(root, 1))

    print(s.find(root, 2))