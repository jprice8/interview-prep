class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def expTree(self, s: str) -> TreeNode:
        nums, ops = [], []
        
        def mockCompute():
            right = nums.pop()
            left = nums.pop()
            op = ops.pop()
            nums.append(TreeNode(val=op, left=left, right=right))

        def precedence(op):
            if op == '+' or op == '-':
                return 1
            elif op == '*' or op == '/':
                return 2
            return 0
        
        i = 0
        while i < len(s):
            # case 1: digit -> parse digits and add to stack
            if s[i].isdigit():
                nums.append(TreeNode(s[i]))
                
            elif s[i] == '(':
                ops.append(s[i])
                
            elif s[i] == ')':
                while ops[-1] != '(': 
                    mockCompute()
                # pop out (
                ops.pop()
            else:
                # operator
                while ops and precedence(ops[-1]) >= precedence(s[i]):
                    mockCompute()
                ops.append(s[i])
            i += 1
        while ops:
            mockCompute()
        return nums[0]

if __name__ == '__main__':
    s = '3*4-2*5'
    sol = Solution()
    print(sol.expTree(s))