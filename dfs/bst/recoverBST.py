from TreeNode import TreeNode


class Solution:
    def recover(self, root):
        def dfs(node):
            nonlocal x, y, pred 
            if node is None:
                return  
            
            dfs(node.left)
            # visit
            if pred and node.val < pred.val:
                y = node 
                # first swap
                if x is None:
                    x = pred 
                else:
                    return 

            pred = node 
            dfs(node.right)

        x = y = pred = None 
        dfs(root)
        x.val, y.val = y.val, x.val
        


if __name__ == '__main__':
    # root = TreeNode(7)
    # root.left = TreeNode(2)
    # root.left.right = TreeNode(5)

    # root.right = TreeNode(11)
    # root.right.left = TreeNode(9)
    # root.right.right = TreeNode(13)

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)

    root.right.left = TreeNode(2)

    s = Solution()
    print(s.recover(root))